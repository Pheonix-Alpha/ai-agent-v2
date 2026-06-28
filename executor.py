import os
from dotenv import load_dotenv
from google import genai
import hashlib
import json

from memory.conversation import save_chat, build_context
from cache.redis_cache import get_cache, set_cache

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def make_cache_key(prompt: str, context: str):
    data = {
        "prompt": prompt.strip().lower(),
        "context": context.strip()
    }
    raw = json.dumps(data, sort_keys=True)
    return hashlib.md5(raw.encode()).hexdigest()


def llm_call(prompt):

    context = build_context()

    cache_key = make_cache_key(prompt, context)

    cached = get_cache(cache_key)

    if cached:
        print("CACHE HIT")
        return cached

    full_prompt = f"""
Conversation History:

{context}

Current Question:

{prompt}
"""

    save_chat("user", prompt)

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=full_prompt
        )
        answer = response.text

    except Exception as e:
        return f"LLM Error: {e}"

    set_cache(cache_key, answer)

    save_chat("assistant", answer)

    return answer
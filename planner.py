import os
import json
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def create_plan(query):

    prompt = f"""
You are an AI planner.

Available tools:

1. search_pdf(query)
2. calculator(expression)

Return ONLY valid JSON.

Example:

[
  {{
    "tool": "search_pdf",
    "input": "ERP"
  }}
]

Question:
{query}
"""

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )
        raw = response.text

    except Exception as e:
        print("LLM Error:", e)
        return []

    print("\nRAW PLAN:\n", raw)

    match = re.search(
        r"\[.*\]",
        raw,
        re.DOTALL
    )

    if not match:
        return []

    try:
        return json.loads(match.group())
    except:
        return []
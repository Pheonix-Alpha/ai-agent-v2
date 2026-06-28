import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def llm_call(prompt):

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )

        return {
            "response": response.text
        }.get(
            "response",
            "No response generated."
        )

    except Exception as e:
        return f"LLM Error: {e}"
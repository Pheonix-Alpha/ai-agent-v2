import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def route_query(query):

    prompt = f"""
You are an AI router.

Available routes:

direct_llm
calculator
search_pdf
planner

Rules:

direct_llm:
- general knowledge
- greetings
- simple explanations

calculator:
- math calculations

search_pdf:
- answer from ERP PDF

planner:
- needs multiple steps/tools

Return ONLY one route.

Question:
{query}
"""

    response = client.models.generate_content(
         model = "gemini-2.5-flash",
        contents=prompt
    )

    raw = response.text.lower()

    if "calculator" in raw:
        return "calculator"

    if "search_pdf" in raw:
        return "search_pdf"

    if "direct_llm" in raw:
        return "direct_llm"

    if "planner" in raw:
        return "planner"

    return "planner"
from llm import llm_call


def classify(query):

    prompt = f"""
Classify the user's question.

Return ONLY one word:

simple
medium
complex

Rules:

simple:
- greetings
- small talk
- basic factual questions

medium:
- requires one tool
- calculator
- pdf search

complex:
- requires multiple steps
- planning
- reasoning
- combining information

Question:
{query}
"""

    result = llm_call(prompt)

    result = result.lower().strip()

    print("CLASSIFIER RAW:", result)

    if "simple" in result:
        return "simple"

    if "medium" in result:
        return "medium"

    if "complex" in result:
        return "complex"

    return "complex"
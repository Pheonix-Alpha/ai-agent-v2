from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # 👈 IMPORTANT FIX

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

models = client.models.list()

for m in models:
    print(m.name)
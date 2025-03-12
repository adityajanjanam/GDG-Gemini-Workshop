from google import genai
from dotenv import load_dotenv
import os
client = genai.Client(api_key="GENAI_API_KEY")

client = genai.Client(api_key="GENAI_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)
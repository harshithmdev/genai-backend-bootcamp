import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_llm_response(user_message: str) -> str:
    prompt = (
        "You are a helpful AI assistant. "
        "Answer clearly and concisely.\n"
        f"User: {user_message}"
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0.3
    )

    return response.output_text
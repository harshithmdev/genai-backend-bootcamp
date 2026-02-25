import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# “Defaults” you can tune later
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4.1-mini")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.3"))
LLM_TIMEOUT_SECONDS = float(os.getenv("LLM_TIMEOUT_SECONDS", "30"))

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Set it in .env or environment variables.")
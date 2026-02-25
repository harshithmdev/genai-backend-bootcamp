import logging
from openai import OpenAI, OpenAIError

from app.core.config import (
    OPENAI_API_KEY,
    LLM_MODEL,
    LLM_TEMPERATURE,
    LLM_TIMEOUT_SECONDS,
)

logger = logging.getLogger(__name__)

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_llm_response(user_message: str) -> str:
    prompt = (
        "You are a helpful AI assistant. "
        "Answer clearly and concisely.\n"
        f"User: {user_message}"
    )

    try:
        logger.info("LLM request started")
        resp = client.responses.create(
            model=LLM_MODEL,
            input=prompt,
            temperature=LLM_TEMPERATURE,
            timeout=LLM_TIMEOUT_SECONDS,
        )
        logger.info("LLM request completed")
        return resp.output_text

    except OpenAIError as e:
        logger.exception("LLM provider error")
        # raise a clean error up to the API layer
        raise RuntimeError("LLM service failed. Please try again.") from e
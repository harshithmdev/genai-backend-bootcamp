import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.llm_service import generate_llm_response

logging.basicConfig(level=logging.INFO)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_id: str

class ChatResponse(BaseModel):
    user_id: str
    user_message: str
    response: str
@app.get("/")
def read_root():
    return {"message": "GenAI Backend Bootcamp Started 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        llm_reply = generate_llm_response(request.message)
        return ChatResponse(
            user_id=request.user_id,
            user_message=request.message,
            response=llm_reply,
        )
    except RuntimeError as e:
        # 503 = service temporarily unavailable
        raise HTTPException(status_code=503, detail=str(e))
from fastapi import FastAPI
from pydantic import BaseModel

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
    return ChatResponse(
        user_id=request.user_id,
        user_message=request.message,
        response=f"You said: {request.message}"
    )
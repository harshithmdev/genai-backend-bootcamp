from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    user_id: str

@app.get("/")
def read_root():
    return {"message": "GenAI Backend Bootcamp Started 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    return {
        "user_message": user_message,
        "response": f"You said: {user_message}"
    }
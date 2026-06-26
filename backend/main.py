from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag import answer_question

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "Saudi Labor Law RAG API is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = answer_question(request.question)
    return {"question": request.question, "answer": answer}
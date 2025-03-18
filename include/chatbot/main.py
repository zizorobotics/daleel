from fastapi import FastAPI, HTTPException
from include.chatbot.chatbot import answer_legal_query


app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Legal Document Chatbot API is working"}

@app.get("/ask/")
def ask_question(user_id: str, question: str):
    """
    Takes a user ID and a question, retrieves the stored document text, and answers.
    """
    answer = answer_legal_query(user_id, question)
    return {"answer": answer}

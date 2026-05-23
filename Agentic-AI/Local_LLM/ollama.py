from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ask")
def ask_llm(question: str):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": question,
            "stream": False
        }
    )

    return {
        "question": question,
        "answer": response.json()["response"]
    }
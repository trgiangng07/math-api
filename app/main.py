from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/question")
def question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    return {
        "question": f"{a} + {b}",
        "answer": a + b
    }
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Query(BaseModel):
    prompt: str


app = FastAPI(title="backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "backend is running"}


@app.post("/ask")
async def ask_llm(query: Query):
    response_text = f"Answer: '{query.prompt}'"
    return {"answer": response_text}

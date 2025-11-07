# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Query(BaseModel):
    prompt: str


app = FastAPI(title="backend-server", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#  TODO: вынести все ендпойнты в отдельный файл endpoints.py


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.post("/send-prompt")
async def ask_llm(query: Query):
    print("Asked: ", query.prompt)

    response_text = f"Answer: 0 eur"  # TODO: ask LLM

    return {"answer": response_text}

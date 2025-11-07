from fastapi import APIRouter
from pydantic import BaseModel

from llm.inference import receiver

router = APIRouter()


class Query(BaseModel):
    prompt: str


@router.post("/send-prompt")
async def ask_llm(query: Query):
    print("Asked:", query.prompt)
    response_text = receiver(query.prompt)
    return {"answer": response_text}

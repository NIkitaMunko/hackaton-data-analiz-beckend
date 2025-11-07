from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.api_endpoints import router as api_router

app = FastAPI(title="backend-server", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Backend is running"}

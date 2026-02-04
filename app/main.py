from fastapi import FastAPI
from .routers import router

app = FastAPI(title="Learning Backend Starter", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(router, prefix="/api/v1")

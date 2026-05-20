from fastapi import FastAPI

from src.api.routes.commands import router as commands_router

app = FastAPI()

app.include_router(commands_router)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

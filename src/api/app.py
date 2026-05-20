from fastapi import FastAPI

from src.api.routes.commands import router as commands_router
from src.api.routes.tags import router as tags_router

app = FastAPI()

app.include_router(commands_router)
app.include_router(tags_router)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

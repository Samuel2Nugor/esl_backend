from fastapi import FastAPI

from src.api.routes.commands import router as commands_router
from src.api.routes.tags import router as tags_router
from src.api.routes.product import router as product_router
from src.api.routes.shelf_location import router as shelf_locations_router
from src.api.routes.assignments import router as assignments_router

app = FastAPI()

app.include_router(commands_router)
app.include_router(tags_router)
app.include_router(product_router)
app.include_router(shelf_locations_router)
app.include_router(assignments_router)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes.commands import router as commands_router
from src.api.routes.tags import router as tags_router
from src.api.routes.product import router as product_router
from src.api.routes.shelf_location import router as shelf_locations_router
from src.api.routes.assignments import router as assignments_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    

app.include_router(commands_router)
app.include_router(tags_router)
app.include_router(product_router)
app.include_router(shelf_locations_router)
app.include_router(assignments_router)

@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

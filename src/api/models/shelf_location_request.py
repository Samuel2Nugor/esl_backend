from pydantic import BaseModel


class ShelfLocationRequest(BaseModel):
    name: str
    description: str | None = None

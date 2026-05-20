from pydantic import BaseModel

class CommandRequest (BaseModel):
    tagId: int
    title: str
    finalPrice: float

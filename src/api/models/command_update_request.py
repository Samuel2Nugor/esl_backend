from pydantic import BaseModel


class CommandUpdateRequest(BaseModel):
    status: str
    

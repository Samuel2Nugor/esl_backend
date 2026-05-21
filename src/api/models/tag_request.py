from pydantic import BaseModel

class TagRequest(BaseModel):
    name: str
    ble_address : str
    status: str = "available"

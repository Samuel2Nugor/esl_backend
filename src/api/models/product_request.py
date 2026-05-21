from pydantic import BaseModel

class ProductRequest(BaseModel):
    sku: str
    name: str
    price: float

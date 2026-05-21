from pydantic import BaseModel



class AssignmentRequest(BaseModel):
    product_id: int
    tag_id: int
    shelf_location_id: int

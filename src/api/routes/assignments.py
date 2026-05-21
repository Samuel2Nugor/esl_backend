from fastapi import APIRouter, HTTPException

from src.api.models.assignment_request import AssignmentRequest
from src.services.assignment_service import (
    create_assignment,
    get_assignment,
    list_assignments,
    update_assignment,
    delete_assignment,
)


router = APIRouter()


@router.post("/assignments")
def create_assignment_route(request: AssignmentRequest) -> dict:
    assignment_id = create_assignment(
        {
            "product_id": request.product_id,
            "tag_id": request.tag_id,
            "shelf_location_id": request.shelf_location_id,
        }
    )
    
    return {
        "status": "created",
        "assignmentId": assignment_id,
    }
    
@router.get("/assignments")
def get_assignments() -> list[dict]:
    return list_assignments()
    

@router.get("/assignments/{assignment_id}")
def get_single_assignment(assignment_id: int) -> dict:
    assignment = get_assignment(assignment_id)
    
    if assignment is None:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found",
        )
        
    return assignment
    
    
@router.patch("/assignments/{assignment_id}")
def update_assignment_route(
    assignment_id: int,
    request: AssignmentRequest,
) -> dict:
    updated = update_assignment(
        assignment_id,
        {
            "product_id": request.product_id,
            "tag_id": request.tag_id,
            "shelf_location_id": request.shelf_location_id,
        },
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found",
        )

    return {
        "status": "updated",
        "assignment": get_assignment(assignment_id),
    }


@router.delete("/assignments/{assignment_id}")
def delete_assignment_route(assignment_id: int) -> dict:
    deleted = delete_assignment(assignment_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found",
        )

    return {
        "status": "deleted",
        "assignmentId": assignment_id,
    }

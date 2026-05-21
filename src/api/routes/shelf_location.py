from fastapi import APIRouter, HTTPException

from src.api.models.shelf_location_request import (
    ShelfLocationRequest,
)
from src.services.shelf_location_service import (
    create_shelf_location,
    delete_shelf_location,
    get_shelf_location,
    list_shelf_locations,
    update_shelf_location,
)

router = APIRouter()


@router.post("/shelf-locations")
def create_location_route(
    request: ShelfLocationRequest,
) -> dict:

    location_id = create_shelf_location(
        {
            "name": request.name,
            "description": request.description,
        }
    )

    return {
        "status": "created",
        "locationId": location_id,
    }


@router.get("/shelf-locations")
def get_locations() -> list[dict]:
    return list_shelf_locations()


@router.get("/shelf-locations/{location_id}")
def get_single_location(
    location_id: int,
) -> dict:

    location = get_shelf_location(location_id)

    if location is None:
        raise HTTPException(
            status_code=404,
            detail="Shelf location not found",
        )

    return location


@router.patch("/shelf-locations/{location_id}")
def update_location_route(
    location_id: int,
    request: ShelfLocationRequest,
) -> dict:

    updated = update_shelf_location(
        location_id,
        {
            "name": request.name,
            "description": request.description,
        },
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Shelf location not found",
        )

    return {
        "status": "updated",
        "location": get_shelf_location(location_id),
    }


@router.delete("/shelf-locations/{location_id}")
def delete_location_route(
    location_id: int,
) -> dict:

    deleted = delete_shelf_location(location_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Shelf location not found",
        )

    return {
        "status": "deleted",
        "locationId": location_id,
    }

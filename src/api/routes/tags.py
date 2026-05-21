from fastapi import APIRouter, HTTPException

from src.api.models.tag_request import TagRequest
from src.services.tag_service import (
    create_tag,
    delete_tag,
    get_tag,
    list_tags,
    update_tag,
)

router = APIRouter()


@router.post("/tags")
def create_tag_route(request: TagRequest) -> dict:
    tag_id = create_tag(
        {
            "name": request.name,
            "ble_address": request.ble_address,
            "status": request.status,
        }
    )

    return {
        "status": "created",
        "tagId": tag_id,
    }


@router.get("/tags")
def get_tags() -> list[dict]:
    return list_tags()


@router.get("/tags/{tag_id}")
def get_single_tag(tag_id: int) -> dict:
    tag = get_tag(tag_id)

    if tag is None:
        raise HTTPException(
            status_code=404,
            detail="Tag not found",
        )

    return tag


@router.patch("/tags/{tag_id}")
def update_tag_route(
    tag_id: int,
    request: TagRequest,
) -> dict:
    updated = update_tag(
        tag_id,
        {
            "name": request.name,
            "ble_address": request.ble_address,
            "status": request.status,
        },
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Tag not found",
        )

    return {
        "status": "updated",
        "tag": get_tag(tag_id),
    }


@router.delete("/tags/{tag_id}")
def delete_tag_route(tag_id: int) -> dict:
    deleted = delete_tag(tag_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Tag not found",
        )

    return {
        "status": "deleted",
        "tagId": tag_id,
    }

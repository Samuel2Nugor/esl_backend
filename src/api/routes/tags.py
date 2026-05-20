from fastapi import APIRouter, HTTPException

from src.services.tag_registry import list_tags, get_tag

router = APIRouter()

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

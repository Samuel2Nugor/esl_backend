from fastapi import APIRouter

from src.api.models.command_request import CommandRequest
from src.services.command_service import publish_command
from src.services.command_history import list_commands

router = APIRouter()

@router.post("/commands")
def create_command(request: CommandRequest) -> dict:
    command_id = publish_command(
        {
            "tagId": request.tagId,
            "title": request.title,
            "finalPrice": request.finalPrice,
        }
    )
    
    if command_id is None:
        return {
            "status": "rejected",
            "reason": "unknown",
        }
    return {
        "status": "published",
        "commandId": command_id,
    }

@router.get("/commands")
def get_commands() -> list[dict]:
    return list_commands()

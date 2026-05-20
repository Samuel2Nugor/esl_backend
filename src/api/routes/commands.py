from fastapi import APIRouter, HTTPException

from src.api.models.command_request import CommandRequest
from src.services.command_service import publish_command
from src.services.command_history import list_commands, get_command_by_id

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

@router.get("/commands/{command_id}")
def get_command(command_id: int) -> dict:
    command = get_command_by_id(command_id)
    
    if command is None:
        raise HTTPException(
            status_code=404,
            detail="Command not found",
        )
    return command

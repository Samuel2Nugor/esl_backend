from fastapi import APIRouter

from src.services.command_service import publish_manual_command

router = APIRouter()

@router.post("/commands")
def create_command() -> dict:
    command_id = publish_manual_command()
    
    if command_id is None:
        return {
            "status": "rejected",
            "reason": "unknown",
        }
    return {
        "status": "published",
        "commandId": command_id,
    }

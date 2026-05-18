from src.command_repository import (
    insert_command, 
    find_command_by_id,
    update_command_status_by_id,
    list_command as repo_list_commands,
)

ALLOWED_STATUSES = {
    "created",
    "published",
    "ack_received",
    "failed",
    "archived",
}

def save_command(payload: dict) -> int:
    return insert_command(payload)
    
    
def update_command_status(command_id: int, status: str) -> bool:
    if status not in ALLOWED_STATUSES:
        return False
    
    return update_command_status_by_id(command_id, status)
        
    
def get_command_by_id(command_id: int) -> dict | None:
    return find_command_by_id(command_id)
    
def archive_command(command_id: int) -> bool:
    return update_command_status(command_id, "archived")
    
def mark_command_ack_received(command_id: int) -> bool:
    return update_command_status(command_id, "ack_received")
    
def list_command() -> list[dict]:
    return repo_list_commands()

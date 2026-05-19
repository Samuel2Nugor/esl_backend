import src.repositories.command_repository as repo

ALLOWED_STATUSES = {
    "created",
    "published",
    "ack_received",
    "failed",
    "archived",
}


def save_command(payload: dict) -> int:
    return repo.insert_command(payload)
    
    
def update_command_status(command_id: int, status: str) -> bool:
    if status not in ALLOWED_STATUSES:
        return False
    
    return repo.update_command_status_by_id(command_id, status)
        
    
def get_command_by_id(command_id: int) -> dict | None:
    return repo.find_command_by_id(command_id)
    
def archive_command(command_id: int) -> bool:
    return repo.update_command_status_by_id(command_id, "archived")
    
def mark_command_ack_received(command_id: int) -> bool:
    return repo.update_command_status_by_id(command_id, "ack_received")
    
def list_commands() -> list[dict]:
    return repo.list_commands()
    
def list_commands_by_status(status: str) -> list[dict]:
    return repo.list_commands_by_status(status)

def list_commands_by_tag(tag_id: int) -> list[dict]:
    return repo.list_commands_by_tag(tag_id)
    
def list_stale_published_commands(timeout_seconds: int) -> list[dict]:
    return repo.list_stale_published_commands(timeout_seconds)
    
def mark_stale_commands_failed(timeout_seconds: int) -> int:
    stale_commands = (
        list_stale_published_commands(timeout_seconds)
    )
    
    updated_count = 0
    
    for command in stale_commands:
        
        increment_retry_count(command["command_id"])
        
        updated = update_command_status(
            command["command_id"], "failed"
        )
        
        if updated:
            updated_count += 1
            
    return updated_count
    
def increment_retry_count(command_id: int) -> bool:
    return repo.increment_retry_count(command_id)
        

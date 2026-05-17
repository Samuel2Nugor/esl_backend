COMMAND_HISTORY = []

NEXT_COMMAND_ID = 1

ALLOWED_STATUSES = {
    "created",
    "published",
    "ack_received",
    "failed",
    "archived",
}

def save_command(payload: dict) -> int:
    global NEXT_COMMAND_ID
    
    command = {
        "command_id": NEXT_COMMAND_ID,
        "payload": payload,
        "status": "created",
    }
    COMMAND_HISTORY.append(command)
    
    NEXT_COMMAND_ID += 1
    
    return command["command_id"]
    
def update_command_status(command_id: int, status: str) -> bool:
    for command in COMMAND_HISTORY:
        if status not in ALLOWED_STATUSES:
            return False
            
        if command["command_id"] == command_id:
            command["status"] = status
            return True
    
    return False
    
def get_command_by_id(command_id: int) -> dict | None:
    for command in COMMAND_HISTORY:
        if command["command_id"] == command_id:
            return command 
            
    return None
    
def archive_command(command_id: int) -> bool:
    for command in COMMAND_HISTORY:
        if command["command_id"] == command_id:
            command["status"] = "archived"
            return True
            
    return False
    
def get_command_history() -> list[dict]:
    return COMMAND_HISTORY

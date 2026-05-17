COMMAND_HISTORY = []

def save_command(payload: dict) -> None:
    COMMAND_HISTORY.append(payload)
    
def get_command_history() -> list[dict]:
    return COMMAND_HISTORY

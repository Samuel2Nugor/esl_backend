from src.command_history import save_command, update_command_status
from src.config import BackendConfig
from src.database import init_db
from src.mqtt_publisher import publish_payload
from src.payload import build_payload, validate_payload
from src.tag_registry import is_known_tag

def publish_manual_command() -> int | None:
    init_db()
    
    config = BackendConfig()
    payload = build_payload(config)
    
    if not is_known_tag(payload["tagId"]):
        print(f"Unknown tagId: {payload['tagId']}. Payload was not published.")
        return None
    
    command_id = save_command(payload)
    payload["commandId"] = command_id
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload: Payload was not published.")
        
    publish_payload(config, payload)
    update_command_status(command_id, "published")
    
    return command_id
    







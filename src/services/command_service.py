from src.config import BackendConfig
from src.services.command_history import save_command, update_command_status
from src.mqtt.mqtt_publisher import publish_payload
from src.contracts.payload import build_payload, validate_payload
from src.services.tag_service import get_tag

# TODO:
# publish_command currently handles multiple responsibilities:
# validation, persistence, queueing, publishing and status updates.
# Consider splitting later if complexity grows

def publish_command(payload: dict) -> int | None:    
    config = BackendConfig()
    
    tag = get_tag(payload["tagId"])
    
    if tag is None:
        print(
            f"Unknown tagId: {payload['tagId']}. "
            "Payload was not published."
        )
        return None
        
    if tag["status"] != "available":
        print(
            f"Unavailable tagId: {payload['tagId']}. "
            "payload was not published."
        )
        return None
        
    command_id = save_command(payload)
    payload["commandId"] = command_id
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload: Payload was not published.")
        
    
        
    publish_payload(config, payload)
    update_command_status(command_id, "published")
    
    return command_id
    


def publish_manual_command() -> int | None:
    config = BackendConfig()
    payload = build_payload(config)
    
    return publish_command(payload)





from src.config import BackendConfig
from src.services.command_history import save_command, update_command_status
from src.mqtt.mqtt_publisher import publish_payload
from src.contracts.payload import build_payload, validate_payload
from src.services.tag_registry import is_known_tag
from src.queue.command_queue import enqueue_command

# TODO:
# publish_command currently handles multiple responsibilities:
# validation, persistence, queueing, publishing and status updates.
# Consider splitting later if complexity grows

def publish_command(payload: dict) -> int | None:    
    config = BackendConfig()
    
    if not is_known_tag(payload["tagId"]):
        print(
            f"Unknown tagId: {payload['tagId']}."
            "Payload was not published."
        )
        return None
    
    command_id = save_command(payload)
    payload["commandId"] = command_id
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload: Payload was not published.")
        
    enqueue_command(command_id)
        
    publish_payload(config, payload)
    update_command_status(command_id, "published")
    
    return command_id
    


def publish_manual_command() -> int | None:
    config = BackendConfig()
    payload = build_payload(config)
    
    return publish_command(payload)





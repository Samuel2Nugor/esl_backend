from src.command_history import save_command, update_command_status
from src.config import BackendConfig
from src.database import init_db
from src.mqtt_publisher import publish_payload
from src.payload import build_payload, validate_payload

def main() -> None:
    init_db()
    
    config = BackendConfig()
    payload = build_payload(config)
    
    command_id = save_command(payload)
    payload["commandId"] = command_id
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload: Payload was not published.")
        
    publish_payload(config, payload)
    update_command_status(command_id, "published")
    
    print(f"Published commandId={command_id} to topic: {config.payload_topic}")
    
if __name__ == "__main__":
    main()

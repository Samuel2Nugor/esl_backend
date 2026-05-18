"""from src.config import BackendConfig
from src.mqtt_publisher import publish_payload
from src.payload import build_payload, validate_payload
from src.command_history import save_command, update_command_status
"""
from src.database import init_db




def main() -> None:
    init_db()
    print("Backend database initialized")
    """config = BackendConfig()
    payload = build_payload(config)
    
    command_id = save_command(payload)
    
    payload["commandId"] = command_id
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload. Payload igored.")
    
    
    publish_payload(config, payload))
    
    update_command_status(command_id, "published"
    
    print(f"Published payload to topic: {config.payload_topic}")
    """

if __name__ == "__main__":
    main()

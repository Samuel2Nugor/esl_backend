from src.config import BackendConfig
from src.mqtt_publisher import publish_payload
from src.payload import build_payload, validate_payload
from src.command_history import save_command





def main() -> None:
    config = BackendConfig()
    payload = build_payload(config)
    
    if not validate_payload(payload):
        raise ValueError("Invalid payload. Payload igored.")
    
    
    command_id = save_command(payload)
    
    publish_payload(config, payload))
    
    update_command_status(command_id, "Published"
    
    print(f"Published payload to topic: {config.payload_topic}")
    

if __name__ == "__main__":
    main()

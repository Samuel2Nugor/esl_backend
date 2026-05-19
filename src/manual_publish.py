from src.config import BackendConfig
from src.services.command_service import publish_manual_command

def main() -> None:
    command_id = publish_manual_command()
    
    if command_id is None:
        return
    
    config = BackendConfig()
    
    print(f"Published commandId={command_id} to topic: {config.payload_topic}")
    
if __name__ == "__main__":
    main()

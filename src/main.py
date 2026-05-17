from config import BackendConfig
from mqtt_publisher import publish_payload
from payload import build_payload





def main() -> None:
    config = BackendConfig()
    payload = build_payload(config)
    
    

    publish_payload(config, payload)
    
    print(f"Published payload to topic: {config.payload_topic}
    

if __name__ == "__main__":
    main()

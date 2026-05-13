from config import BackendConfig
from mqtt_publisher import MqttPublisher





def main() -> None:
    config = BackendConfig()
    
    payload = {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }
    
    publisher = MqttPublisher(config)
    publisher.publish_payload(payload)
    
    print(f"Published payload to topic: {config.topic}")
    

if __name__ == "__main__":
    main()

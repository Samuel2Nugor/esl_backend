from config import BackendConfig
#from mqtt_publisher import publish_payload
from ack_listener import listen_for_ack





def main() -> None:
    config = BackendConfig()
    listen_for_ack(config)
    """payload = {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }

    publish_payload(config, payload)
    
    print(f"Published payload to topic: {config.payload_topic}")"""
    

if __name__ == "__main__":
    main()

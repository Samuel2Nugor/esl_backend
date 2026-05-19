import json
import paho.mqtt.client as mqtt

from src.config import BackendConfig

def publish_payload(config: BackendConfig, payload: dict) -> None:
    message = json.dumps(payload)
    
    client = mqtt.Client()
    client.connect(
        config.broker_host,
        config.broker_port,
        keepalive=60,
    )
    
    result = client.publish(config.payload_topic, message)
    
    if result.rc != mqtt.MQTT_ERR_SUCCESS:
        client.disconnect()
        raise RuntimeError(f"Failed to publish MQTT message. rc={result.rc}")
        
    client.disconnect()

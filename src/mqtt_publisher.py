import json
import paho.mqtt.client as mqtt

from config import BackendConfig

class MqttPublisher:
    def __init__(self, config: BackendConfig) -> None:
        self.config = config
        self.client = mqtt.Client()
        
    def publish_payload(self, payload: dict) -> None:
        message = json.dumps(payload)
        
        self.client.connect(
            self.config.broker_host,
            self.config.broker_port,
            keepalive=60
        )
        
        result = self.client.publish(self.config.topic, message)
        
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            raise RuntimeError(f"Failed to publish MQTT message. rc={result.rc}")
            
        self.client.disconnect()

import json
import paho.mqtt.client as mqtt

from src.config import BackendConfig

def listen_for_ack(config: BackendConfig) -> None:
    def on_connect(client, userdata, flags, rc, properties=None) -> None:
        if rc == 0:
            print("Connected to MQTT broker")
            client.subscribe(config.ack_topic)
            print(f"Subcribed to ACK topic: {config.ack_topic}")
        else:
            print(f"Failed to connect to MQTT broker. rc={rc}")
    
    def on_message(client, userdata, msg) -> None:
        try:
            payload_text = msg.payload.decode("utf-8")
            data = json.loads(payload_text)
            
            print("ACK received:")
            print(f"   topic: {msg.topic}")
            print(f"   tagId: {data.get('tagId')}")
            print(f"   ack: {data.get('ack')}")
            
        except UnicodeDecodeError:
            print("Could not decode ACK payload")
        except json.JSONDecodeError:
            print("ACK payload is not valid JSON")
            
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(
        config.broker_host,
        config.broker_port,
        keepalive=60,
    )
    
    print("Waiting for ACK messages...")
    client.loop_forever()

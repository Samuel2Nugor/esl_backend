from src.config import BackendConfig
from src.mqtt_publisher import publish_payload

def test_publish_payload_function_exists():
    config = BackendConfig()
    
    payload = {
        "commandId": 1,
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }
    
    assert callable(publish_payload)
    assert payload["commandId"] == 1
    assert payload["tagId"] == config.tag_id

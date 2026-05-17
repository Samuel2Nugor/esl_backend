from src.config import BackendConfig
from src.payload import build_payload, validate_payload, validate_ack_payload

def test_build_payload_returns_gateway_contract():
    config = BackendConfig()
    payload = build_payload(config)

    assert payload == {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }
    
def test_validate_payload_accepts_valid_payload():
    payload = {
        "commandId": 1,
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    assert validate_payload(payload) is True
    
def test_validate_payload_rejects_missing_field():
    payload = {
        "commandId": 1,
        "tagId": 1,
        "title": "Milk 1L",
    }
    
    assert validate_payload(payload) is False
    
def test_validate_payload_rejects_wrong_type():
    payload = {
        "commandId": 1,
        "tagId": "1",
        "title": 2,
        "finalPrice": 29.00,
    }
    
    assert validate_payload(payload) is False
    
def test_validate_ack_payload_accepts_command_id():
    payload = {
        "commandId": 1,
        "tagId": 1,
        "ack": "true",
    }
    
    assert validate_ack_payload(payload) is True

from src.config import BackendConfig
from src.payload import build_payload

def test_build_payload_returns_gateway_contract():
    config = BackendConfig()
    payload = build_payload(config)

    assert payload == {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }

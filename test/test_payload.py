from src.config import BackendConfig


def test_payload_has_required_gateway_fields():
    config = BackendConfig()
    
    payload = {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice":config.final_price,
    }
    
    assert "tagId" in payload
    assert "title" in payload
    assert "finalPrice" in payload

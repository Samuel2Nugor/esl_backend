from src.config import BackendConfig

def test_config_has_mqtt_topics():
    config = BackendConfig()
    
    assert config.payload_topic == "esl/tag/write"
    assert config.ack_topic == "esl/tag/ack"

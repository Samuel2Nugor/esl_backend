from src.ack_listener import listen_for_ack
from src.config import BackendConfig


def test_listen_for_ack_function_exists():
    config = BackendConfig()
    
    assert callable(listen_for_ack)
    assert config.ack_topic == "esl/tag/ack"

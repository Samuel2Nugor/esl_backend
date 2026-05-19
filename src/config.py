from dataclasses import dataclass

@dataclass(frozen=True)
class BackendConfig:
    broker_host: str = "localhost"
    broker_port: int = 1883
    payload_topic: str = "esl/tag/write"
    ack_topic: str = "esl/tag/ack" 
    
    tag_id: int = 999
    title: str = "Milk 1L"
    final_price: float = 29.00

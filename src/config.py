from dataclasses import dataclass

@dataclass(frozen=True)
class BackendConfig:
    broker_host: str = "localhost"
    broker_port: int = 1883
    topic: str = "esl/tag/write"
    
    tag_id: int = 1
    title: str = "Milk 1L"
    final_price: float = 29.00

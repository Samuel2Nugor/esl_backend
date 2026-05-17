from src.config import BackendConfig



def build_payload(config: BackendConfig) -> dict:
    return {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }

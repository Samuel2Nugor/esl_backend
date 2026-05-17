from src.config import BackendConfig



def build_payload(config: BackendConfig) -> dict:
    return {
        "tagId": config.tag_id,
        "title": config.title,
        "finalPrice": config.final_price,
    }
    
def validate_payload(payload: dict) -> bool:
    required_fields = ["commandId", "tagId", "title", "finalPrice"]
    
    for field in required_fields:
        if field not in payload:
            return False
            
    if not isinstance(payload["commandId"], int):
        return False
            
    if not isinstance(payload["tagId"], (int, str)):
        return False
    
    if not isinstance(payload["title"], str):
        return False
        
    if not isinstance(payload["finalPrice"], (int, float)):
        return False
        
    return True
    
def validate_ack_payload(payload: dict) -> bool:
    required_fields = ["commandId", "tagId", "ack"]
    
    for field in required_fields:
        if field not in payload:
            return False
    
    if not isinstance(payload["commandId"], int):
        return False
    
    if not isinstance(payload["tagId"], int):
        return False
        
    if not isinstance(payload["ack"], str):
        return False
        
    if payload["ack"].lower() not in ("true", "false"):
        return False
    
    return True
    

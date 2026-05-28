

# Contract

def build_payload(command_id: int, tag_id: int, title: str, final_price: float) -> dict:
    return {
        "commandId": command_id,
        "tagId": tag_id,
        "title": title,
        "finalPrice": final_price,
    }
    
def validate_payload(payload: dict) -> bool:
    required_fields = ["commandId", "tagId", "title", "finalPrice"]
    
    for field in required_fields:
        if field not in payload:
            return False
            
    if not isinstance(payload["commandId"], int):
        return False
            
    if not isinstance(payload["tagId"], int):
        return False
    
    if not isinstance(payload["title"], str):
        return False
        
    if not isinstance(payload["finalPrice"], (float, int)):
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
    

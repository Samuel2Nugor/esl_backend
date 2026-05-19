KNOWN_TAGS = {
    1: {
        "name": "TG_01",
        "address": "74:4D:BD:63:C2:C6"
    }
    
}

def is_known_tag(tag_id: int) -> bool:
    return tag_id in KNOWN_TAGS
    
def get_tag_address(tag_id: int) -> str | None:
    tag = KNOWN_TAGS.get(tag_id)
    if tag is None:
        return None
        
    return tag["address"]

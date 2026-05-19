from src.tag_registry import get_tag_address, is_known_tag


def test_known_tag_returns_true():
    assert is_known_tag(1) is True
    
def test_unknown_tag_returns_false():
    assert is_known_tag(2000) is False

def test_known_tag_returns_address():
    assert get_tag_address(1) == "74:4D:BD:63:C2:C6"
    
def test_unkown_tag_returns_none():
    assert get_tag_address(2000) is None

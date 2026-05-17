from src.tag_registry import is_known_tag

def test_known_tag_is_acceptted():
    assert is_known_tag(1) is True
    
def test_unknown_tag_is_rejected():
    assert is_known_tag(999) is False

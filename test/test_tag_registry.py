from src.services.tag_registry import get_tag_address, is_known_tag, list_tags, get_tag


def test_known_tag_returns_true():
    assert is_known_tag(1) is True
    
def test_unknown_tag_returns_false():
    assert is_known_tag(2000) is False

def test_known_tag_returns_address():
    assert get_tag_address(1) == "74:4D:BD:63:C2:C6"
    
def test_unkown_tag_returns_none():
    assert get_tag_address(2000) is None
    
def test_list_tags_returns_known_tags():
    tags = list_tags()
    
    assert tags == [
        {
            "tagId": 1,
            "name": "TG_01",
            "address": "74:4D:BD:63:C2:C6",
        }
    ]
    
def test_get_tag_return_known_tag():
    tag = get_tag(1)
    
    assert tag == {
        "tagId": 1,
        "name": "TG_01",
        "address": "74:4D:BD:63:C2:C6",
    }
    
def test_get_tag_returns_none_for_unknown_tag():
    assert get_tag(3000) is None

from src.command_history import COMMAND_HISTORY, get_command_history, save_command

def test_save_command_adds_payload_to_history():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    save_command(payload)
    
    assert get_command_history() == [payload]

from src.command_history import (
    COMMAND_HISTORY, 
    get_command_history, 
    save_command,
    archive_command,
    get_command_by_id,
    update_command_status,
    mark_command_ack_received,
)

def test_save_command_adds_payload_to_history():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    history = get_command_history()
    
    assert len(history) == 1
    assert history[0]["command_id"] == command_id
    assert history[0]["payload"] == payload
    assert history [0]["status"] == "created"
    
def test_update_command_status_changes_status():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    updated = update_command_status(command_id, "published")
    
    history = get_command_history()
    
    assert updated is True
    assert history[0]["status"] == "published"
    
def test_update_command_status_returns_false_for_unknown_command():
    COMMAND_HISTORY.clear()
    
    updated = update_command_status(999, "failed")
    
    assert updated is False
    
def test_get_command_by_id_returns_command():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    command = get_command_by_id(command_id)
    
    assert command is not None
    assert command["command_id"] == command_id
    
def test_archive_command_updates_status():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    archived = archive_command(command_id)
    
    command = get_command_by_id(command_id)
    
    assert archived is True
    assert command["status"] == "archived"

def test_mark_command_ack_received_updates_exact_command():
    COMMAND_HISTORY.clear()
    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    updated = mark_command_ack_received(command_id)
    command = get_command_by_id(command_id)
    
    assert updated is True
    assert command["status"] == "ack_received"
    
def test_mark_command_ack_received_returns_false_for_unknown_command():
    COMMAND_HISTORY.clear()
    
    updated = mark_command_ack_received(999)
    
    assert updated is False

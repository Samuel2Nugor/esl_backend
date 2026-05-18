from src.command_history import (
    save_command,
    archive_command,
    get_command_by_id,
    update_command_status,
    mark_command_ack_received,
)
from src.database import init_db, get_connection

def setup_function():
    init_db()
    
    with get_connection() as conn:
        conn.execute("DELETE FROM commands")
        conn.commit()

def test_save_command_adds_payload_to_history():    
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    command = get_command_by_id(command_id)
    
    assert command is not None
    assert command["command_id"] == command_id
    assert command["tagId"] == 1
    assert command["title"] == "Milk 1L"
    assert command["finalPrice"] == 29.00
    assert command["status"] == "created"
    
def test_update_command_status_changes_status():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    updated = update_command_status(command_id, "published")    
    command = get_command_by_id(command_id)
    
    assert updated is True
    assert command["status"] == "published"
    
def test_update_command_status_returns_false_for_unknown_command():
    updated = update_command_status(999, "failed")
    
    assert updated is False
    
def test_get_command_status_rejects_invalid_status():   
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    updated = update_command_status(command_id, "car")
    
    assert updated is False

def test_get_command_by_id_returns_none_for_unknown_command():
    command = get_command_by_id(2000)
    
    assert command is None
    
def test_archive_command_updates_status():
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
    updated = mark_command_ack_received(999)
    
    assert updated is False

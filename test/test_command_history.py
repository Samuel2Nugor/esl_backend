from src.command_history import (
    save_command,
    archive_command,
    get_command_by_id,
    update_command_status,
    mark_command_ack_received,
    list_commands,
    list_commands_by_status,
    list_commands_by_tag,
    list_stale_published_commands,
    mark_stale_commands_failed,
    increment_retry_count,
)

from src.database import init_db, get_connection

#----------- TEST-------------#

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
    
def test_list_commands_returns_saved_commands():
    payload_1 = {
        "tagId": 1,
        "title": "Bread",
        "finalPrice": 29.00,
    }
    
    payload_2 = {
        "tagId": 1,
        "title": "Bread",
        "finalPrice": 29.00,
    }
    
    command_id_1 = save_command(payload_1)
    command_id_2 = save_command(payload_2)
    
    commands = list_commands()
    
    command_ids = [command["command_id"] for command in commands]
    
    assert command_id_1 in command_ids
    assert command_id_2 in command_ids
    
def test_list_commands_by_status_return_only_matching_status():
    payload_1 = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    payload_2 = {
        "tagId": 1,
        "title": "Bread",
        "finalPrice": 19.00,
    }
    
    command_id_1 = save_command(payload_1)
    command_id_2 = save_command(payload_2)
    
    update_command_status(command_id_1, "published")
    
    published_commands = list_commands_by_status("published")
    
    command_ids = [command["command_id"] for command in published_commands]
    
    assert command_id_1 in command_ids
    assert command_id_2 not in command_ids
    
def test_list_commands_by_tag_returns_only_matching_tag():
    payload_1 = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    payload_2 = {
        "tagId": 2,
        "title": "Bread",
        "finalPrice": 19.00,
    }
    
    command_id_1 = save_command(payload_1)
    command_id_2 = save_command(payload_2)
    
    tag_1_commands = list_commands_by_tag(1)
    
    command_ids = [command["command_id"] for command in tag_1_commands]
    
    assert command_id_1 in command_ids
    assert command_id_2 not in command_ids
    
def test_list_stale_published_commands_returns_published_commands():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    update_command_status(command_id, "published")
    
    stale_commands = list_stale_published_commands(0)
    
    command_ids = [ command["command_id"] for command in stale_commands]
    
    assert command_id in command_ids
    
def test_mark_stale_commands_failed():
    payload = {
        "tagId": 1,
        "title": "Orange juice 1L",
        "finalPrice": 18.00,
    }
    
    command_id = save_command(payload)
    update_command_status(command_id, "published")
    
    updated_count = mark_stale_commands_failed(0)
    
    command = get_command_by_id(command_id)
    
    assert updated_count == 1
    assert command["status"] == "failed"
    assert command["retry_count"] == 1
    
def test_save_command_sets_retry_count_to_zero():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    command = get_command_by_id(command_id)
    
    assert command["retry_count"] == 0
    
def test_increment_retry_count_updates_value():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    increment_retry_count(command_id)
    
    command = get_command_by_id(command_id)
    
    assert command["retry_count"] == 1
    

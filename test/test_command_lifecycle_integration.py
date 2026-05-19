from src.command_history import(
    get_command_by_id,
    mark_stale_commands_failed,
    save_command,
    update_command_status,
    mark_command_ack_received,
)
from src.database import get_connection, init_db

def setup_functon():
    init_db()
    
    with get_connection() as conn:
        conn.execute("DELETE FROM commands")
        conn.commit()
        
def test_command_lifecycle_published_then_failed_after_timeout():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    
    published = update_command_status(command_id, "published")
    failed_count = mark_stale_commands_failed(timeout_seconds=0)
    
    command = get_command_by_id(command_id)
    
    assert published is True
    assert failed_count == 1
    assert command["status"] == "failed"
    assert command["retry_count"] == 1
    
def test_command_lifecycle_then_ack_received():
    payload = {
        "tagId": 1,
        "title": "Milk 1L",
        "finalPrice": 29.00,
    }
    
    command_id = save_command(payload)
    published = update_command_status(command_id, "published")
    acked = mark_command_ack_received(command_id)
    
    command = get_command_by_id(command_id)
    
    assert published is True
    assert acked is True
    assert command["status"] == "ack_received"
    assert command["retry_count"] == 0
    

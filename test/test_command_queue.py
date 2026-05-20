from src.queue.command_queue import (
    enqueue_command,
    dequeue_command,
    queue_size,
    clear_queue,
)

def test_queue_add_and_remove():
    clear_queue()
    
    enqueue_command(123)
    
    assert queue_size() == 1
    
    command_id = dequeue_command()
    
    assert command_id == 123
    assert queue_size() == 0

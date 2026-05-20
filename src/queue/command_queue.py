from queue import Queue

command_queue = Queue()


def enqueue_command(command_id: int) -> None:
    command_queue.put(command_id)
    
def dequeue_command() -> int:
    return command_queue.get()
    
def queue_size() -> int:
    return command_queue.qsize()
    
def clear_queue() -> None:
    while not command_queue.empty():
        command_queue.get()

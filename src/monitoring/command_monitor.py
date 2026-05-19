import time

from src.services.command_history import mark_stale_commands_failed

def check_stale_commands(timeout_seconds: int=30) -> int:
    return mark_stale_commands_failed(timeout_seconds)

def run_command_monitor(timeout_seconds: int=10, interval_seconds: int=3,) -> None:
    print("Command monitor started")
    
    while True:
        updated_count = mark_stale_commands_failed(timeout_seconds)
        
        if updated_count > 0:
            print(f"Marked {updated_count} stale commands(s) as failed")
            
        time.sleep(interval_seconds)
        
if __name__ == "__main__":
    run_command_monitor()

import time

from src.command_history import mark_stale_commands_failed

def run_command_monitor(timeout_seconds: int=30, interval_seconds: int=5,) -> None:
    
    while True:
        updated_count = mark_stale_commands_failed(timeout_seconds)
        
        if updated_count > 0:
            print(
                f"Marked {updated_count} stale commands(s) as failed"
            )
            
        time.sleep(interval_seconds)

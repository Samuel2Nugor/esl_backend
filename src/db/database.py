import sqlite3
from datetime import datetime

DB_PATH = "data/backend.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
    
def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                final_price REAL NOT NULL,
                status TEXT NOT NULL,
                retry_count INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        
        conn.commit()
    
def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")

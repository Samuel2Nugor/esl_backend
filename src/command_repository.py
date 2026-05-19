from datetime import datetime
from src.database import get_connection, _now


# row helper
def _row_to_command(row) -> dict:
    return {
        "command_id": row[0],
        "tagId": row[1],
        "title": row[2],
        "finalPrice": row[3],
        "status": row[4],
        "created_at": row[5],
        "updated_at": row[6],
    }
    
# SQL command functions
def insert_command(payload: dict) -> int:
    now = _now()
    
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO commands (
                tag_id,
                title,
                final_price,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                payload["tagId"],
                payload["title"],
                payload["finalPrice"],
                "created",
                now,
                now,
            ),
        )
        
        return cursor.lastrowid
        
def find_command_by_id(command_id: int) -> dict | None:
    with get_connection() as conn:
        conn.row_factory = None
        cursor = conn.execute(
            """
            SELECT id, tag_id, title, final_price, status, created_at, updated_at
            FROM commands
            WHERE id = ?
            """,
            (command_id,),
        )
        
        row = cursor.fetchone()
    
    if row is None:
        return None
        
    return _row_to_command(row)

def update_command_status_by_id(command_id: int, status: str) -> bool:
    now = _now()
    
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE commands
            SET status = ?, updated_at = ?
            WHERE id = ?
            """,
            (status, now, command_id),
        )
        
        return cursor.rowcount == 1
        
def list_commands() -> list [dict]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT id, tag_id, title, final_price,status, created_at, updated_at
            FROM commands
            ORDER BY id DESC
            """
        )
        
        rows = cursor.fetchall()
        
    return [_row_to_command(row) for row in rows]

def list_commands_by_status(status: str) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT id, tag_id, title, final_price, status, created_at, updated_at
            FROM commands
            WHERE status = ?
            ORDER BY id DESC
            """,
            (status,),
        )
        
        rows = cursor.fetchall()
        
    return [_row_to_command(row) for row in rows]
    
def list_commands_by_tag(tag_id: int) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT id, tag_id, title, final_price, status, created_at, updated_at
            FROM commands
            WHERE tag_id = ?
            ORDER BY id DESC
            """,
            (tag_id,),
        )
        rows = cursor.fetchall()
        
    return [_row_to_command(row) for row in rows]

def list_stale_published_commands(timeout_seconds: int) -> list[dict]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT id, tag_id, title, final_price, status, created_at, updated_at
            FROM commands
            WHERE status = 'published'
            """
        )
        
        rows = cursor.fetchall()
    
    stale_commands = []
    
    now = datetime.now()
    
    for row in rows:
        updated_at = datetime.fromisoformat(row[6])
        
        age_seconds = (now - updated_at).total_seconds()
        if age_seconds >= timeout_seconds:
            stale_commands.append(_row_to_command(row))
            
    return stale_commands
            

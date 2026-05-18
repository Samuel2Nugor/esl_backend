from src.database import get_connection, _now

ALLOWED_STATUSES = {
    "created",
    "published",
    "ack_received",
    "failed",
    "archived",
}

def save_command(payload: dict) -> int:
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
    
def update_command_status(command_id: int, status: str) -> bool:
    if status not in ALLOWED_STATUSES:
        return False
    
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
        
    
def get_command_by_id(command_id: int) -> dict | None:
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
        
    return {
        "command_id": row[0],
        "tagId": row[1],
        "title": row[2],
        "finalPrice": row[3],
        "status": row[4],
        "created_at": row[5],
        "updated_at": row[6],
    }
    
def archive_command(command_id: int) -> bool:
    return update_command_status(command_id, "archived")
    
def mark_command_ack_received(command_id: int) -> bool:
    return update_command_status(command_id, "ack_received")
    

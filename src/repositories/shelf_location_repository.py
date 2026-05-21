from src.db.database import get_connection, _now


#--------- Row helper function---------#

def _row_to_shelf_location(row) -> dict:
    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "created_at": row[3],
        "updated_at": row[4],
    }


def insert_shelf_location(location: dict) -> int:
    now = _now()
    
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO shelf_locations (
                name,
                description,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                location["name"],
                location.get("description"),
                now,
                now,
            ),
        )
        
        conn.commit()
        return cursor.lastrowid
        
def find_shelf_location_by_id(location_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT id, name, description, created_at, updated_at
            FROM shelf_locations
            WHERE id = ?
            """,
            (location_id,),
        ).fetchone()
        
    if row is None:
        return None
            
    return _row_to_shelf_location(row)
    
def list_shelf_locations() -> list[dict]:
    with get-connection() as conn:
        rows = conn.execute(
            """"
            SELECT id, name, description, created_at, updated_at
            FROM shelf_locations
            """
        ).fetchall()
        
    return [_row_to_shelf_location(row) for row in rows]
    
def update_shelf_location(location_id: int, location: dict) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE shelf_locations
            SET name = ?, description = ?, updated_at = ?
            WHERE id = ?
            """,
            (
                location["name"],
                location.get("description"),
                _now(),
                location_id,
            ),
        )
        
        conn.commit()
        return cursor.rowcount > 0
        
def delete_shelf_location(location_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            DELETE FROM shelf_locations
            WHERE id = ?
            """,
            (location_id,),
        )
        
        conn.commit()
        return cursor.rowcount > 0
    

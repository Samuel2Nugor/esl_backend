from src.db.database import get_connection, _now

def _row_to_tag(row) -> dict:
    return {
        "id": row[0],
        "name": row[1],
        "ble_address": row[2],
        "status": row[3],
        "created_at": row[4],
        "updated_at": row[5],
    }


def insert_tag(tag: dict) -> int:
    now = _now()

    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO tags (
                name,
                ble_address,
                status,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                tag["name"],
                tag["ble_address"],
                tag.get("status", "available"),
                now,
                now,
            ),
        )

        conn.commit()
        return cursor.lastrowid


def find_tag_by_id(tag_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT id, name, ble_address, status, created_at, updated_at
            FROM tags
            WHERE id = ?
            """,
            (tag_id,),
        ).fetchone()

    if row is None:
        return None

    return _row_to_tag(row)


def list_tags() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, name, ble_address, status, created_at, updated_at
            FROM tags
            """
        ).fetchall()

    return [_row_to_tag(row) for row in rows]


def update_tag(tag_id: int, tag: dict) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE tags
            SET name = ?, ble_address = ?, status = ?, updated_at = ?
            WHERE id = ?
            """,
            (
                tag["name"],
                tag["ble_address"],
                tag["status"],
                _now(),
                tag_id,
            ),
        )

        conn.commit()
        return cursor.rowcount > 0


def delete_tag(tag_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            DELETE FROM tags
            WHERE id = ?
            """,
            (tag_id,),
        )

        conn.commit()
        return cursor.rowcount > 0



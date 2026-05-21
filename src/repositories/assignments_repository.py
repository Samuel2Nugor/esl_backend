from src.db.database import get_connection, _now




def _row_to_assignment(row) -> dict:
    return {
        "id": row[0],
        "product_id": row[1],
        "tag_id": row[2],
        "shelf_location_id": row[3],
        "created_at": row[4],
        "updated_at": row[5],
    }



def create_assignment(assignment: dict) -> int:
    now = _now()

    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO product_tag_shelf_assignments (
                product_id,
                tag_id,
                shelf_location_id,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                assignment["product_id"],
                assignment["tag_id"],
                assignment["shelf_location_id"],
                now,
                now,
            ),
        )

        conn.commit()
        return cursor.lastrowid


def get_assignment(assignment_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT
                id,
                product_id,
                tag_id,
                shelf_location_id,
                created_at,
                updated_at
            FROM product_tag_shelf_assignments
            WHERE id = ?
            """,
            (assignment_id,),
        ).fetchone()

    if row is None:
        return None

    return _row_to_assignment(row)


def list_assignments() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id,
                product_id,
                tag_id,
                shelf_location_id,
                created_at,
                updated_at
            FROM product_tag_shelf_assignments
            """
        ).fetchall()

    return [_row_to_assignment(row) for row in rows]
    
    
def update_assignment(assignment_id: int, assignment: dict) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE product_tag_shelf_assignments
            SET product_id = ?,
                tag_id = ?,
                shelf_location_id = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                assignment["product_id"],
                assignment["tag_id"],
                assignment["shelf_location_id"],
                _now(),
                assignment_id,
            ),
        )

        conn.commit()
        return cursor.rowcount > 0


def delete_assignment(assignment_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            DELETE FROM product_tag_shelf_assignments
            WHERE id = ?
            """,
            (assignment_id,),
        )

        conn.commit()
        return cursor.rowcount > 0



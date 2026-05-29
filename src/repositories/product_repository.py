from src.db.database import get_connection, _now


def insert_product(product: dict) -> int:
    now = _now()

    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO products (
                sku,
                name,
                price,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                product["sku"],
                product["name"],
                product["price"],
                now,
                now,
            ),
        )

        conn.commit()
        return cursor.lastrowid


def find_product_by_id(product_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT
                id,
                sku,
                name,
                price,
                created_at,
                updated_at
            FROM products
            WHERE id = ?
            """,
            (product_id,)
        ).fetchone()

    if row is None:
        return None

    return {
        "id": row[0],
        "sku": row[1],
        "name": row[2],
        "price": row[3],
        "created_at": row[4],
        "updated_at": row[5]
    }


def list_products() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id,
                sku,
                name,
                price,
                created_at,
                updated_at
            FROM products
            """
        ).fetchall()

    return [
        {
            "id": row[0],
            "sku": row[1],
            "name": row[2],
            "price": row[3],
            "created_at": row[4],
            "updated_at": row[5]
        }
        for row in rows
    ]


def update_product(product_id: int, product: dict) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            UPDATE products
            SET sku = ?, name = ?, price = ?, updated_at = ?
            WHERE id = ?
            """,
            (
                product["sku"],
                product["name"],
                product["price"],
                _now(),
                product_id,
            ),
        )

        conn.commit()
        return cursor.rowcount > 0


def delete_product(product_id: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            DELETE FROM products
            WHERE id = ?
            """,
            (product_id,),
        )

        conn.commit()
        return cursor.rowcount > 0

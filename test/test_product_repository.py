from src.db.database import get_connection, init_db
from src.repositories.product_repository import (
    insert_product,
    find_product_by_id,
    list_products,
)


def setup_function():
    init_db()

    with get_connection() as conn:
        conn.execute("DELETE FROM products")
        conn.commit()


def test_insert_product_returns_id():
    product_id = insert_product(
        {
            "sku": "MILK001",
            "name": "Milk 1L",
            "price": 29.0,
        }
    )

    assert isinstance(product_id, int)


def test_find_product_by_id_returns_product():
    product_id = insert_product(
        {
            "sku": "MILK001",
            "name": "Milk 1L",
            "price": 29.0,
        }
    )

    product = find_product_by_id(product_id)

    assert product["id"] == product_id
    assert product["sku"] == "MILK001"
    assert product["name"] == "Milk 1L"
    assert product["price"] == 29.0


def test_list_products_returns_saved_products():
    insert_product(
        {
            "sku": "MILK001",
            "name": "Milk 1L",
            "price": 29.0,
        }
    )

    products = list_products()

    assert len(products) == 1
    assert products[0]["sku"] == "MILK001"

from src.db.database import init_db

from src.services.product_service import create_product
from src.services.tag_service import create_tag
from src.services.shelf_location_service import create_shelf_location
from src.services.assignment_service import create_assignment


def seed_tags() -> None:
    create_tag({
        "name": "TG_01",
        "ble_address": "74:4D:BD:63:C2:C6",
        "status": "available",
    })

    create_tag({
        "name": "TG_02",
        "ble_address": "74:4D:BD:63:C2:C7",
        "status": "available",
    })

    create_tag({
        "name": "TG_03",
        "ble_address": "74:4D:BD:63:C2:C8",
        "status": "available",
    })


def seed_products() -> None:
    create_product({
        "sku": "CHEESE-001",
        "name": "Cheddar Cheese",
        "price": 39.90,
    })

    create_product({
        "sku": "MILK-001",
        "name": "Milk 1L",
        "price": 29.00,
    })

    create_product({
        "sku": "APPLE-001",
        "name": "Apple 2kg",
        "price": 59.00,
    })


def seed_shelf_locations() -> None:
    create_shelf_location({
        "name": "Dairy Aisle - Cheese Section",
        "description": "Refrigerated dairy shelf for cheese products.",
    })

    create_shelf_location({
        "name": "Dairy Aisle - Milk Section",
        "description": "Refrigerated shelf for milk and dairy drinks.",
    })

    create_shelf_location({
        "name": "Produce Section - Fruit Display",
        "description": "Fresh fruit display near produce entrance.",
    })


def seed_assignments() -> None:
    create_assignment({
        "product_id": 1,
        "tag_id": 1,
        "shelf_location_id": 1,
    })

    create_assignment({
        "product_id": 2,
        "tag_id": 2,
        "shelf_location_id": 2,
    })

    create_assignment({
        "product_id": 3,
        "tag_id": 3,
        "shelf_location_id": 3,
    })


def main() -> None:
    init_db()

    seed_tags()
    seed_products()
    seed_shelf_locations()
    seed_assignments()

    print("Demo data seeded successfully.")


if __name__ == "__main__":
    main()

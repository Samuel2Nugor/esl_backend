from src.services.product_service import (
    create_product,
    get_product,
    update_product,
    delete_product,
)

from src.services.tag_service import (
    create_tag,
    get_tag,
    update_tag,
    delete_tag,
)

from src.services.shelf_location_service import (
    create_shelf_location,
    get_shelf_location,
    update_shelf_location,
    delete_shelf_location,
)


def test_product_crud_lifecycle():

    product = {
        "sku": "TEST001",
        "name": "Milk 1L",
        "price": 29.0,
    }

    product_id = create_product(product)

    created = get_product(product_id)

    assert created["name"] == "Milk 1L"

    update_product(
        product_id,
        {
            "sku": "TEST001",
            "name": "Milk 2L",
            "price": 35.0,
        },
    )

    updated = get_product(product_id)

    assert updated["name"] == "Milk 2L"

    deleted = delete_product(product_id)

    assert deleted is True
    assert get_product(product_id) is None


def test_tag_crud_lifecycle():

    tag = {
        "name": "TG_01",
        "ble_address": "74:4D:BD:63:C2:C6",
        "status": "available",
    }

    tag_id = create_tag(tag)

    created = get_tag(tag_id)

    assert created["name"] == "TG_01"

    update_tag(
        tag_id,
        {
            "name": "TG_02",
            "ble_address": "74:4D:BD:63:C2:C7",
            "status": "available",
        },
    )

    updated = get_tag(tag_id)

    assert updated["name"] == "TG_02"

    deleted = delete_tag(tag_id)

    assert deleted is True
    assert get_tag(tag_id) is None


def test_shelf_location_crud_lifecycle():

    location = {
        "name": "Dairy A1",
        "description": "Milk shelf",
    }

    location_id = create_shelf_location(location)

    created = get_shelf_location(location_id)

    assert created["name"] == "Dairy A1"

    update_shelf_location(
        location_id,
        {
            "name": "Dairy A2",
            "description": "Updated shelf",
        },
    )

    updated = get_shelf_location(location_id)

    assert updated["name"] == "Dairy A2"

    deleted = delete_shelf_location(location_id)

    assert deleted is True
    assert get_shelf_location(location_id) is None

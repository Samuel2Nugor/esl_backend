from fastapi.testclient import TestClient
from src.db.database import get_connection, init_db
from unittest.mock import patch
from src.api.app import app


def setup_function():
    init_db()

    with get_connection() as conn:
        conn.execute("DELETE FROM commands")
        conn.execute("DELETE FROM products")
        conn.execute("DELETE FROM tags")
        conn.execute("DELETE FROM shelf_locations")
        conn.execute("DELETE FROM product_tag_shelf_assignments")
        conn.commit()
#-----------------Unit testing-----------#
client = TestClient(app)

def test_health_endpoint_returns_ok():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def _create_test_tag():
    response = client.post(
        "/tags",
         json={
            "name": "TG_01",
            "ble_address": "74:4D:BD:63:C2:C6",
            "status": "available",
        },
    )
    assert response.status_code == 200
    return response.json()["tagId"]
        
    
def test_get_tags_returns_created_tags():
    create_response = client.post(
        "/tags",
        json={
            "name": "TG_01",
            "ble_address": "74:4D:BD:63:C2:C6",
            "status": "available",
        },
    )

    assert create_response.status_code == 200

    response = client.get("/tags")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "TG_01"
    assert data[0]["ble_address"] == "74:4D:BD:63:C2:C6"
    assert data[0]["status"] == "available"


def test_get_single_tag_returns_created_tag():
    create_response = client.post(
        "/tags",
        json={
            "name": "TG_01",
            "ble_address": "74:4D:BD:63:C2:C6",
            "status": "available",
        },
    )

    tag_id = create_response.json()["tagId"]

    response = client.get(f"/tags/{tag_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == tag_id
    assert data["name"] == "TG_01"
    assert data["ble_address"] == "74:4D:BD:63:C2:C6"
    assert data["status"] == "available"
    
def test_get_single_tag_returns_404_for_unknown_tag():
    response = client.get("/tags/999")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Tag not found"}
        
#--------Command endpoints API test-----------#

def test_get_commands_returns_empty_list_when_no_commands():
    response = client.get("/commands")
    
    assert response.status_code == 200
    assert response.json() == []
    
def test_post_commands_creates_commands():
    tag_id = _create_test_tag()
    
    with patch("src.services.command_service.publish_payload"):
        response = client.post(
            "/commands",
            json={
                "tagId": tag_id,
                "title":"Coffee",
                "finalPrice": 39.00,
            },
        )
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["status"] == "published"
    assert isinstance(data["commandId"], int)
    
def test_get_single_command_returns_command():
    tag_id = _create_test_tag()
    
    with patch("src.services.command_service.publish_payload"):
        create_response = client.post(
            "/commands",
            json={
                "tagId": tag_id,
                "title":"Milk 1L",
                "finalPrice": 29.00,
            },
        )
    
    command_id = create_response.json()["commandId"]
    response = client.get(f"/commands/{command_id}")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["command_id"] == command_id
    assert data["tagId"] == tag_id
    assert data["title"] == "Milk 1L"
    assert data["finalPrice"] == 29.00
    
def test_patch_command_updates_status():
    tag_id = _create_test_tag()
    
    with patch("src.services.command_service.publish_payload"):
        create_response = client.post(
            "/commands",
            json={
                "tagId": tag_id,
                "title": "Coffee",
                "finalPrice": 39.00,
            },
        )

    command_id = create_response.json()["commandId"]

    response = client.patch(
        f"/commands/{command_id}",
        json={
            "status": "ack_received"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "updated"
    assert data["command"]["status"] == "ack_received"


def test_delete_command_archives_command():
    tag_id = _create_test_tag()
    
    with patch("src.services.command_service.publish_payload"):
        create_response = client.post(
            "/commands",
            json={
                "tagId": tag_id,
                "title": "Coffee",
                "finalPrice": 39.00,
            },
        )

    command_id = create_response.json()["commandId"]

    response = client.delete(f"/commands/{command_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "archived"
    assert data["command"]["status"] == "archived"
    
def _create_assignment_test_data():
    product_response = client.post(
        "/products",
        json={
            "sku": "ASSIGN001",
            "name": "Milk 1L",
            "price": 29.0,
        },
    )
    product_id = product_response.json()["productId"]

    tag_response = client.post(
        "/tags",
        json={
            "name": "TG_01",
            "ble_address": "74:4D:BD:63:C2:C6",
            "status": "available",
        },
    )
    tag_id = tag_response.json()["tagId"]

    shelf_response = client.post(
        "/shelf-locations",
        json={
            "name": "Dairy A1",
            "description": "Milk section",
        },
    )
    shelf_location_id = shelf_response.json()["locationId"]

    return product_id, tag_id, shelf_location_id
    

from fastapi.testclient import TestClient
from src.db.database import get_connection, init_db

from src.api.app import app


def setup_function():
    init_db()
    
    with get_connection() as conn:
        conn.execute("DELETE FROM commands")
        conn.commit()
#-----------------Unit testing-----------#
client = TestClient(app)

def test_health_endpoint_returns_ok():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def test_get_tags_returns_known_tags():
    response = client.get("/tags")
    
    assert response.status_code == 200
    assert response.json() == [
        {
            "tagId": 1,
            "name": "TG_01",
            "address": "74:4D:BD:63:C2:C6",
        }
    ]
    
def test_get_single_tag_returns_known_tag():
    response = client.get("/tags/1")
    
    assert response.status_code == 200
    assert response.json() == {
            "tagId": 1,
            "name": "TG_01",
            "address": "74:4D:BD:63:C2:C6",
    }
    
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
    response = client.post(
        "/commands",
        json={
            "tagId": 1,
            "title":"Coffee",
            "finalPrice": 39.00,
        },
    )
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["status"] == "published"
    assert isinstance(data["commandId"], int)
    
def test_get_single_command_returns_command():
    create_response = client.post(
        "/commands",
        json={
            "tagId": 1,
            "title":"Milk 1L",
            "finalPrice": 29.00,
        },
    )
    
    command_id = create_response.json()["commandId"]
    response = client.get(f"/commands/{command_id}")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["command_id"] == command_id
    assert data["tagId"] == 1
    assert data["title"] == "Milk 1L"
    assert data["finalPrice"] == 29.00
    
def test_patch_command_updates_status():
    create_response = client.post(
        "/commands",
        json={
            "tagId": 1,
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
    create_response = client.post(
        "/commands",
        json={
            "tagId": 1,
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

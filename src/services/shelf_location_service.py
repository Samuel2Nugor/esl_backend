from src.repositories.shelf_location_repository import (
    delete_shelf_location as repo_delete_shelf_location,
    find_shelf_location_by_id,
    insert_shelf_location,
    list_shelf_locations as repo_list_shelf_locations,
    update_shelf_location as repo_update_shelf_location,
)

def create_shelf_location(location: dict) -> int:
    return insert_shelf_location(location)
    
def get_shelf_location(location_id: int) -> dict | None:
    return find_shelf_location_by_id(location_id)
    
def list_shelf_locations() -> list[dict]:
    return repo_list_shelf_locations()
    
def update_shelf_location(location_id: int, location: dict) -> bool:
    return repo_update_shelf_location(location_id, location,)
    
def delete_shelf_location(location_id: int) -> bool:
    return repo_delete_shelf_location(location_id)

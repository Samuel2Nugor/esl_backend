from src.repositories.assignments_repository import (
    create_assignment as repo_create_assignment,
    get_assignment as repo_get_assignment,
    list_assignments as repo_list_assignments,
    update_assignment as repo_update_assignment,
    delete_assignment as repo_delete_assignment,
)


def create_assignment(assignment: dict) -> int:
    return repo_create_assignment(assignment)


def get_assignment(assignment_id: int) -> dict | None:
    return repo_get_assignment(assignment_id)


def list_assignments() -> list[dict]:
    return repo_list_assignments()
    

def update_assignment(assignment_id: int, assignment: dict) -> bool:
    return repo_update_assignment(assignment_id, assignment)
    
def delete_assignment(assignment_id: int) -> bool:
    return repo_delete_assignment(assignment_id)
    

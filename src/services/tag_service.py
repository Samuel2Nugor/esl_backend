from src.repositories.tag_repository import (
    delete_tag as repo_delete_tag,
    find_tag_by_id,
    insert_tag,
    list_tags as repo_list_tags,
    update_tag as repo_update_tag,
)


def create_tag(tag: dict) -> int:
    return insert_tag(tag)


def get_tag(tag_id: int) -> dict | None:
    return find_tag_by_id(tag_id)


def list_tags() -> list[dict]:
    return repo_list_tags()


def update_tag(tag_id: int, tag: dict) -> bool:
    return repo_update_tag(tag_id, tag)


def delete_tag(tag_id: int) -> bool:
    return repo_delete_tag(tag_id)

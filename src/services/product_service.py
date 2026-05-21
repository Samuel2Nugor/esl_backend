from src.repositories.product_repository import(
    find_product_by_id,
    insert_product,
    list_products as repo_list_products,
    update_product as repo_update_product,
    delete_product as repo_delete_product,
    
)

def create_product(product: dict) -> int:
    return insert_product(product)
    
def get_product(product_id: int) -> dict | None:
    return find_product_by_id(product_id)
    
def list_products() -> list[dict]:
    return repo_list_products()
    
def update_product(product_id: int, product: dict) -> bool:
    return repo_update_product(product_id, product)
    
def delete_product(product_id: int) -> bool:
    return repo_delete_product(product_id)

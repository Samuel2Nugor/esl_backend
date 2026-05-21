from fastapi import APIRouter, HTTPException

from src.api.models.product_request import ProductRequest
from src.services.product_service import (
    create_product,
    get_product,
    list_products,
    update_product,
    delete_product,
)

router = APIRouter()

@router.post("/products")
def create_product_route(request: ProductRequest) -> dict:
    product_id = create_product(
        {
            "sku": request.sku,
            "name": request.name,
            "price": request.price,
        }
    )
    
    return {
        "status": "created",
        "productId": product_id,
    }
    
@router.get("/products")
def get_products() -> list[dict]:
    return list_products()
    

@router.get("/products/{product_id}")
def get_single_product(product_id: int) -> dict:
    product = get_product(product_id)
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
        
    return product
    
@router.patch("/products/{product_id}")
def update_product_route(
    product_id: int,
    request: ProductRequest,
) -> dict:
    updated = update_product(
        product_id,
        {
            "sku": request.sku,
            "name": request.name,
            "price": request.price,
        },
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    product = get_product(product_id)

    return {
        "status": "updated",
        "product": product,
    }


@router.delete("/products/{product_id}")
def delete_product_route(product_id: int) -> dict:
    deleted = delete_product(product_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return {
        "status": "deleted",
        "productId": product_id,
    }
    


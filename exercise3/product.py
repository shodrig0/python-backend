from pydantic import BaseModel
from fastapi import APIRouter
from typing import Optional
from data import data

router = APIRouter()

# ProductCreate, ProductUpdate, ProductResponse, ProductPatch
# create != update
class Product(BaseModel):
    id: int
    description: Optional[str] = None
    price: Optional[float] = None
    sku: Optional[int] = None
    stock: Optional[int] = None

@router.post("/product")
async def create_product(product: Product):
    data.append(product.model_dump()) # python fastapi dict
    return product

@router.get("/product")
async def get_product():
    return data

@router.get("/product/{id}")
async def get_product_by_id(id: int):
    for product in data:
        if product["id"] == id:
            return product
    return { "msg": "No data" } # i can use HTTPException(status_code = 404, detail = "No data")

@router.put("/product/{id}")
async def put_product_by_id(id: int, product: Product):
    for product_id, prod in enumerate(data): # obtain index
        if prod["id"] == id:
            data[product_id] = product.model_dump()
            return data[product_id]
    return { "msg": "No data" }

@router.patch("/product/{id}")
async def patch_product_by_id(id: int, product: Product):
    for product_id, prod in enumerate(data):
        if prod["id"] == id:
            update_data = product.model_dump(exclude_unset = True)
            prod.update(update_data)
            return data[product_id]
    return { "msg": "No data" }

@router.delete("/product/{id}")
async def delete_product_by_id(id: int):
    for product_id, product in enumerate(data):
        if product["id"] == id:
            data.pop(product_id)
            return { "msg": "OK" }
    return { "msg": "No data" }

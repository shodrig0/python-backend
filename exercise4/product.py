from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Optional, List
from data import data

product_router = APIRouter()

class ProductCreate(BaseModel):
    id: int
    description: str
    price: float
    region: str
    sku: int
    stock: int

class ProductUpdate(BaseModel):
    description: Optional[str] = None
    price: Optional[float] = None
    region_id: Optional[int] = None # check
    sku: Optional[int] = None
    stock: Optional[int] = None

@product_router.get("/product")
async def get_product(region: str | None = None):
    data_list = data
    if region is not None:
        new_list = []
        for product in data_list:
           if region.lower() == product["region"].lower():
               new_list.append(product)
        data_list = new_list
    return data_list

@product_router.get("/product/{id}")
async def get_product_by_id(id: str):
    for product in data:
        if product["id"] == int(id):
            return product
    raise HTTPException(status_code = 404, detail = "No data")

@product_router.post("/product")
async def create_product(product: ProductCreate):
    data.append(product.model_dump())
    return product

@product_router.put("/product/{id}")
async def put_product_by_id(id: int, product: ProductUpdate):
    for product_id, prod in enumerate(data):
        if prod["id"] == id:
            data[product_id] = product.model_dump()
            return data[product_id]
    raise HTTPException(status_code = 404, detail = "No data")

@product_router.patch("/product/{id}")
async def patch_product_by_id(id: int, product: ProductUpdate):
    for product_id, prod in enumerate(data):
        if prod["id"] == id:
            update_data = product.model_dump(exclude_unset = True)
            prod.update(update_data)
            return data[product_id]
    raise HTTPException(status_code = 404, detail = "No data")

@product_router.delete("/product/{id}")
async def delete_product_by_id(id: int):
    for product_id, product in enumerate(data):
        if product["id"] == id:
            data.pop(product_id)
            return { "msg": "Successfully removed" }
    raise HTTPException(status_code = 404, detail = "No data")
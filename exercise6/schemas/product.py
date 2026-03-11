from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from services.initializer import get_session
from services.product import get_all_products, get_product_by_sku, get_products_by_title, create_product, delete_product_by_sku, modify_data_product_by_sku

product_router = APIRouter()

class ProductCreate(BaseModel):
    sku: str
    title: str
    description: str
    image: str

    category_name: str

    model_config = ConfigDict(from_attributes = True)

class ProductUpdate(BaseModel):
    sku: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None

    category_name: Optional[str] = None

    model_config = ConfigDict(from_attributes = True)

@product_router.post('/products')
async def create_product_by_api(product_model: ProductCreate, session: Session = Depends(get_session)):
    product_data = product_model.model_dump()
    
    product = create_product(session, product_data)

    if not product:
        raise HTTPException(status_code = 400, detail = 'Bad request')
    
    return product

@product_router.get('/products')
async def read_products(title: str | None = None, session: Session = Depends(get_session)):
    if title:
        return get_products_by_title(session, title)
    
    return get_all_products(session)

@product_router.get('/products/{product_sku}')
async def read_product_by_sku(product_sku: str, session: Session = Depends(get_session)):
    product = get_product_by_sku(session, product_sku)

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    return product

@product_router.patch('/products/{product_sku}')
async def update_product(product_sku: str, product_update: ProductUpdate, session: Session = Depends(get_session)):
    update_data = product_update.model_dump(exclude_unset = True)
    
    product = modify_data_product_by_sku(session, product_sku, update_data)

    if not product:
        raise HTTPException(status_code = 404, detail = "Product not found")

    return product

@product_router.delete('/products/{product_sku}')
async def delete_product(product_sku: str, session: Session = Depends(get_session)):
    product = delete_product_by_sku(session, product_sku)

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    return { "detail": "Product deleted successfully" }
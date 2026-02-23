from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from services.initializer import get_session
from services.product import get_all_products, get_product_by_sku, update_description_product, create_product, delete_product_by_sku, get_products_by_description, order_product_by_description

product_router = APIRouter()
class ProductResponse(BaseModel):
    description: str
    sku: str

    model_config = ConfigDict(from_attributes = True)

class ProductUpdate(BaseModel):
    description: Optional[str] = None
    sku: Optional[str] = None

    model_config = ConfigDict(from_attributes = True)


@product_router.post('/products')
async def create_product_by_api(product: ProductResponse, session: Session = Depends(get_session)):
    product = create_product(session, product.description, product.sku)
    
    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    return product

@product_router.get('/products')
async def read_products(description: str | None = None, order: str | None = None, session: Session = Depends(get_session)):
    if description:
        return get_products_by_description(session, description)
    
    if order and order.lower() == 'asc':
        return order_product_by_description(session)
    
    return get_all_products(session)

@product_router.get('/products/{product_sku}')
async def read_product_by_sku(product_sku: str, session: Session = Depends(get_session)):
    product = get_product_by_sku(session, product_sku)

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    return product

@product_router.patch('/products/{product_sku}')
async def update_description_product_by_sku(product_sku: str, product_description: ProductUpdate, session: Session = Depends(get_session)):
    product = update_description_product(session, product_sku, product_description)

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    product.description = product_description.description
    session.commit()
    session.refresh(product)
    return product

@product_router.delete('/products/{product_sku}')
async def delete_product(product_sku: str, session: Session = Depends(get_session)):
    product = delete_product_by_sku(session, product_sku)

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    session.commit()
    return HTTPException(status_code = 200, detail = 'Product deleted successfully')
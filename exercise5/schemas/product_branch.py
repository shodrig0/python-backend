from pydantic import BaseModel, ConfigDict
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from services.initializer import get_session
from services.product_branch import get_all_product_branch, group_products_branch, modify_stock_of_product

product_branch_router = APIRouter()
class ProductBranchResponse(BaseModel):
    branch_id: str
    product_id: str
    stock: int

    model_config = ConfigDict(from_attributes = True)

class ProductBranchCreate(BaseModel):
    sku_product: str
    pc_branch: str
    stock: int

class ProductBranchUpdate(BaseModel):
    branch_id: Optional[str] = None
    product_id: Optional[str] = None
    stock: Optional[int] = None

    model_config = ConfigDict(from_attributes = True)

@product_branch_router.get('/product-branch')
async def read_product_branch(session: Session = Depends(get_session)):
    return get_all_product_branch(session)

@product_branch_router.post('/product-branch')
async def create_product_branch(product_branch: ProductBranchCreate, session: Session = Depends(get_session)):
    product_branch = group_products_branch(session, product_branch.sku_product, product_branch.pc_branch, product_branch.stock)

    if not product_branch:
        raise HTTPException(status_code = 404, detail = 'Not found')

    return product_branch

@product_branch_router.patch('/product-branch/{sku_product}/{pc_branch}')
async def modify_stock_product_branch(sku_product: str, pc_branch: str, product_stock: ProductBranchUpdate, session: Session = Depends(get_session)):
    product_branch = modify_stock_of_product(session, sku_product, pc_branch, product_stock.stock)

    if not product_branch:
        raise HTTPException(status_code = 404, detail = 'Not found')
    
    product_branch.stock = product_stock.stock
    return product_branch

# @product_branch_router.delete('/product_branch')
# async def delete_product_branch_by_():
#     return
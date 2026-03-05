from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.initializer import get_session
from services.price import get_current_price, update_price

price_router = APIRouter()
class PriceResponse(BaseModel):
    amount: float
    valid_from: datetime
    valid_to: datetime
    product_id: int
    branch_id: int

    model_config = ConfigDict(from_attributes = True)

class PriceCreate(BaseModel):
    amount: float
    valid_from: datetime
    valid_to: datetime
    product_id: int
    branch_id: int

    model_config = ConfigDict(from_attributes = True)

class PriceUpdate(BaseModel):
    amount: Optional[float] = None
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None
    product_id: Optional[int] = None
    branch_id: Optional[int] = None

    model_config = ConfigDict(from_attributes = True)

@price_router.get('/price/{sku_product}/{pc_branch}')
async def get_price_product(sku_product: str, pc_branch: str, session: Session = Depends(get_session)):
    return get_current_price(session, sku_product, pc_branch)

@price_router.patch('/price/{sku_product}/{pc_branch}')
async def get_price_product(sku_product: str, pc_branch: str, price_amount: PriceUpdate, session: Session = Depends(get_session)):
    price = update_price(session, sku_product, pc_branch, price_amount.amount)

    if not price:
        raise HTTPException(status_code = 404, detail = 'Not found')
    
    price.amount = price_amount.amount

    return price
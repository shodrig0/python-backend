from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from services.initializer import get_session
from services.fakestore import import_products
from utils.fakestore_scraper import fakestore_scraper

fakestore_router = APIRouter()

class FakestoreCreate(BaseModel):
    sku: str
    title: str
    description: str
    image: str
    category_name: str
    price: Decimal

    model_config = ConfigDict(from_attributes = True)

@fakestore_router.post('/fakestore')
async def seed_db(session: Session = Depends(get_session)):
    products = fakestore_scraper("https://fakestoreapi.com/products")
    import_products(session, products)

    if not products:
        raise HTTPException(status_code = 404, detail = "Product not found")

    return {"detail": "Products were imported"}
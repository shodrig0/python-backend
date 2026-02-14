from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class Product(BaseModel):
    id: int
    description: str
    price: float
    sku: int | None = None
    stock: int

@router.post("/product/")
async def create_product(product: Product):
    return product

@router.get("/product/", response_model = list[Product])
async def get_product() -> list[Product]:
    return [ Product(id = 1, description = "Milk", price = 50, sku = 12345, stock = 10) ]

# finish later
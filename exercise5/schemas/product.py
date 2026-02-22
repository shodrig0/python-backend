from pydantic import BaseModel, ConfigDict
from fastapi import APIRouter

product_router = APIRouter()
class ProductResponse(BaseModel):
    product_id: int
    description: str
    sku: str

    model_config = ConfigDict(from_attributes = True)
from pydantic import BaseModel, ConfigDict

class ProductResponse(BaseModel):
    product_id: int
    description: str
    sku: str

    model_config = ConfigDict(from_attributes = True)
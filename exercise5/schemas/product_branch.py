from pydantic import BaseModel, ConfigDict

class ProductBranch(BaseModel):
    branch_id: int
    product_id: int
    stock: int

    model_config = ConfigDict(from_attributes = True)
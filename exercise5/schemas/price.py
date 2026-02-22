from pydantic import BaseModel, ConfigDict
from datetime import date

class Price(BaseModel):
    price_id: int
    amount: float
    valid_from: date
    valid_to: date
    product_id: int
    branch_id: int

    model_config = ConfigDict(from_attributes = True)
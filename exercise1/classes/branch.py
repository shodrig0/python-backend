from dataclasses import dataclass
from typing import List
from classes.product import Product

@dataclass
class Branch:
    id: int
    city: str
    postal_code: str
    product: List["Product"]
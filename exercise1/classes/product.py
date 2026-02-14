from dataclasses import dataclass
from typing import List
from classes.price import Price

@dataclass
class Product:
    id: int
    description: str
    sku: str
    stock: int
    price: List["Price"]

    def get_current_price(self) -> Price:
        return max(self.price, key = lambda p: p.timestamp)
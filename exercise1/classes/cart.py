from dataclasses import dataclass
from .product import Product

@dataclass
class Cart:
    amount: int = 0
    total: float = 0.0

    def add(self, quantity: int, product: Product) -> float:
        unit_value = product.price[0].value
        self.amount += quantity
        self.total += quantity * unit_value
        return self.total
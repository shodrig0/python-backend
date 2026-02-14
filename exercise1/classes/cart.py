from dataclasses import dataclass
from .product import Product

@dataclass
class Cart:
    amount: int = 0
    total: float = 0.0

    def add(self, quantity: int, product: Product) -> float:

        if quantity < 1:
            raise ValueError("Buy more than 1")

        elif quantity > product.stock:
            raise ValueError("Insufficient stock")
        
        unit_value = product.get_current_price().value
        self.amount += quantity
        self.total += quantity * unit_value
        return self.total
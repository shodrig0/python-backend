from dataclasses import dataclass
from typing import List
from classes.product import Product

@dataclass
class Branch:
    id: int
    city: str
    postal_code: str
    product: List["Product"]



    # If price depends here > change Product -> Price
    # def get_current_price(self, branch: Branch) -> Price:
    #     branch_prices_list = [
    #         p for p in self.price if p.branch == branch
    #     ]
    #     return max(branch_prices_list, key = lambda p: p.timestamp)
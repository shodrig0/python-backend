from sqlalchemy.orm import Session
from services.product import get_product_by_sku
from services.product_branch import get_one_product_branch, group_products_branch
from utils.fakestore_scraper import fakestore_scraper
from utils.fakestore_mapper import fakestore_mapper
from services.price import modify_price
from decimal import Decimal
import random

def update_price(session: Session):
    products = fakestore_scraper("https://fakestoreapi.com/products")

    for product in products:
        data = fakestore_mapper(product)
        product = get_product_by_sku(session, data["sku"])

        base_price = data["price"]
        variation = Decimal(str(random.uniform(-0.03, 0.03)))

        new_price = Decimal(base_price) * (Decimal("1") + variation)
        modify_price(session, product.sku, "NY-123", new_price)
        print("Updated prices")
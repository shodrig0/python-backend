from sqlalchemy.orm import Session
from utils.fakestore_mapper import fakestore_mapper
from services.category import get_category_by_name, create_category
from services.product import get_product_by_sku, create_product
from services.product_branch import group_products_branch, get_one_product_branch
from services.price import create_price


def import_products(session: Session, products: list):

    for product in products:

        data = fakestore_mapper(product)

        category = get_category_by_name(session, data["category_name"])

        if not category:
            category = create_category(session, data["category_name"])

        product = get_product_by_sku(session, data["sku"])

        if not product:
            product = create_product(session, data)

        # fakestore does not have branches or stock
        relation = get_one_product_branch(session, product.sku, "NY-123")

        if not relation:
            relation = group_products_branch(session, product.sku, "NY-123", stock = 100)

        create_price(session, relation, data["price"])
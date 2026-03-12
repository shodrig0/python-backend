from sqlalchemy.orm import Session
from utils.fakestore_mapper import fakestore_mapper
from services.category import get_category_by_name, create_category
from services.product import get_product_by_sku, create_product
from services.branch import get_branch_by_postal_code, create_branch
from services.product_branch import group_products_branch, get_one_product_branch
from services.price import create_price
from utils.default_postal_code import DEFAULT_POSTAL_CODE


def import_products(session: Session, products: list):

    branch = get_branch_by_postal_code(session, DEFAULT_POSTAL_CODE)

    if not branch:
        branch = create_branch(session, "New York", DEFAULT_POSTAL_CODE)

    for product in products:

        data = fakestore_mapper(product)

        category = get_category_by_name(session, data["category_name"])

        if not category:
            category = create_category(session, data["category_name"])

        product = get_product_by_sku(session, data["sku"])

        if not product:
            product = create_product(session, data)

        # fakestore does not have branches or stock
        relation = get_one_product_branch(session, product.sku, branch.postal_code)

        if not relation:
            relation = group_products_branch(session, product.sku, branch.postal_code, stock = 100)

        create_price(session, relation, data["price"])
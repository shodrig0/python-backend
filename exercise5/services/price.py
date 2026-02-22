from services.initializer import session
from models.price import Price
from models.product import Product
from models.branch import Branch
from models.product_branch import ProductBranch
from datetime import datetime, timezone


def create_price(product_sku, pc_branch, amount, valid_from, valid_to):
    product_branch = (
        session.query(ProductBranch).join(Product).join(Branch).filter(Product.sku == product_sku, Branch.postal_code == pc_branch).first()
    )

    if not product_branch:
        raise ValueError('Not Found')

    price = Price(amount = amount, valid_from = valid_from, valid_to = valid_to, product_branch = product_branch)
    session.add(price)
    return price

def update_price(product_sku, pc_branch, new_amount):
    product_branch = (
        session.query(ProductBranch).join(Product).join(Branch).filter(Product.sku == product_sku, Branch.postal_code == pc_branch).first()
    )

    if not product_branch:
        raise ValueError('Not Found')

    current_price = (
        session.query(Price).filter(Price.product_id == product_branch.product_id, Price.branch_id == product_branch.branch_id, Price.valid_to.is_(None)).one_or_none()
    )

    now = datetime.now(timezone.utc)

    if current_price:
        current_price.valid_to = now

    new_price = Price(amount = new_amount, valid_from = now, valid_to = None, product_branch = product_branch)
    session.add(new_price)
    return new_price
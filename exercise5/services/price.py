from services.initializer import session
from models.price import Price
from models.product import Product
from models.branch import Branch
from models.product_branch import ProductBranch

def create_price(product_sku, pc_branch, amount, valid_from, valid_to):
    product_branch = (
        session.query(ProductBranch).join(Product).join(Branch).filter(Product.sku == product_sku, Branch.postal_code == pc_branch).first()
    )

    if not product_branch:
        raise ValueError('Not Found')

    price = Price(amount = amount, valid_from = valid_from, valid_to = valid_to, product_branch = product_branch)
    session.add(price)
    return price
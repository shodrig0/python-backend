from services.initializer import session
from models.product_branch import ProductBranch
from models.product import Product
from models.branch import Branch

def define_product_branch(product, branch, stock):
    product_branch = ProductBranch(product = product, branch = branch, stock = stock)

    if not product_branch:
        raise ValueError('No Data')

    return product_branch

def group_products_branch(sku_product, pc_branch, stock):
    product = session.query(Product).filter_by(sku = sku_product).first()
    branch = session.query(Branch).filter_by(postal_code = pc_branch).first()

    if not product:
        raise ValueError('No Data')

    if not branch:
        raise ValueError('No Data')

    product_branch = ProductBranch(product = product, branch = branch, stock = stock)
    session.add(product_branch)

    return product_branch
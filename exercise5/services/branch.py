from services.initializer import session
from models.branch import Branch

def create_branch(city, postal_code):
    branch = Branch(city = city, postal_code = postal_code)
    session.add(branch)
    return branch

def get_product_by_postal_code(postal_code):
    product = session.query(Branch).filter_by(postal_code = postal_code).first()
    return product

# work in progress...
from services.initializer import session
from models.product import Product

def create_product(description, sku):
    product = Product(description = description, sku = sku)
    return product

def get_all_products():
    products = session.query(Product).all()
    return products

def get_product_by_description(description):
    product = session.query(Product).filter(Product.description.like(f"%{description}%")).all()
    return product
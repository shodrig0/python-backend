from services.initializer import session
from models.product import Product

def create_product(description, sku):
    product = Product(description = description, sku = sku)
    session.add(product)
    return product

def get_all_products():
    products = session.query(Product).all()

    if not products:
        raise ValueError('No Data')

    return products

def get_product_by_sku(sku):
    product = session.query(Product).filter_by(sku = sku).first()

    if not product:
        raise ValueError('No Data')

    return product

def get_products_by_description(description):
    products = session.query(Product).filter(Product.description.like(f"%{description}%")).all()

    if not products:
        raise ValueError('No Data')

    return products

def order_product_by_description():
    products = session.query(Product).order_by(Product.description).all()

    if not products:
        raise ValueError('No Data')

    return products

def update_description_product(sku, new_description):
    product = session.query(Product).filter_by(sku = sku).first()

    if not product:
        raise ValueError('No Data')
    
    product.description = new_description
    return product

def delete_product_by_sku(sku):
    product = session.query(Product).filter_by(sku = sku).first()
    
    if not product:
        return None
    
    session.delete(product)
    return True
# from services.initializer import session
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.product import Product

def create_product(session: Session, description: str, sku: str):
    product = Product(description = description, sku = sku)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_all_products(session: Session):
    products = session.query(Product).all()

    if not products:
        raise HTTPException(status_code = 404, detail = 'Products not found')

    return products

def get_product_by_sku(session: Session, sku: str):
    product = session.query(Product).filter_by(sku = sku).first()

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')

    return product

def get_products_by_description(session: Session, description: str):
    products = session.query(Product).filter(Product.description.ilike(f"%{description}%")).all()

    if not products:
        raise HTTPException(status_code = 404, detail = 'Products not found')
    
    return products

def order_product_by_description(session: Session):
    products = session.query(Product).order_by(Product.description).all()

    if not products:
        raise HTTPException(status_code = 404, detail = 'Products not found')

    return products

def update_description_product(session: Session, sku: str, new_description: str):
    product = session.query(Product).filter_by(sku = sku).first()

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    product.description = new_description
    return product

def delete_product_by_sku(session: Session, sku: str):
    product = session.query(Product).filter_by(sku = sku).first()
    
    if not product:
        return None
    
    session.delete(product)
    return True
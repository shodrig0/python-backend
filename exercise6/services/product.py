from sqlalchemy.orm import Session
from models.product import Product
from services.category import get_category_by_name

def create_product(session: Session, product_data: dict):
    category = get_category_by_name(session, product_data["category_name"])

    product = Product(sku = product_data["sku"], title = product_data["title"], description = product_data["description"], image = product_data["image"], category = category)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_all_products(session: Session):
    products = session.query(Product).all()
    return products

def get_product_by_sku(session: Session, sku: str):
    product = session.query(Product).filter_by(sku = sku).first()

    if not product:
        raise None

    return product

def get_products_by_title(session: Session, title: str):
    products = session.query(Product).filter(Product.title.ilike(f"%{title}%")).all()

    if not products:
        raise None
    
    return products

def modify_data_product_by_sku(session: Session, sku: str, update_data: dict): # dictionary
    product = get_product_by_sku(session, sku)

    if not product:
        return None
    
    if "title" in update_data:
        product.title = update_data["title"]
    if "description" in update_data:
        product.description = update_data["description"]
    if "image" in update_data:
        product.image = update_data["image"]
    if "category_name" in update_data:
        category = get_category_by_name(session, update_data["category_name"])
        product.category = category

    session.commit()
    session.refresh(product)
    return product

def delete_product_by_sku(session: Session, sku: str):
    product = get_product_by_sku(session, sku)

    if not product:
        return None

    session.delete(product)
    session.commit()
    return True
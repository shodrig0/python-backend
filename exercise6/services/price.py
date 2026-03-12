from sqlalchemy.orm import Session
from models.price import Price
from models.product_branch import ProductBranch
from services.product_branch import get_one_product_branch
from datetime import datetime, timezone
from decimal import Decimal

def create_price(session: Session, product_branch: ProductBranch, amount: Decimal):
    now = datetime.now(timezone.utc)

    price = Price(amount = amount, valid_from = now, valid_to = None, product_branch = product_branch)
    session.add(price)
    session.commit()
    session.refresh(price)
    return price

def get_all_prices(session: Session):
    return session.query(Price).all()

def get_current_price(session: Session, product_sku: str, pc_branch: str):
    product_branch = get_one_product_branch(session, product_sku, pc_branch)

    if not product_branch:
        return None
    
    price = (
        session.query(Price).filter(Price.product_branch_id == product_branch.product_branch_id, Price.valid_to.is_(None)).one_or_none()
    )

    return price

def modify_price(session: Session, product_sku: str, pc_branch: str, new_amount: Decimal):
    product_branch = get_one_product_branch(session, product_sku, pc_branch)

    if not product_branch:
        return None

    current_price = (
        session.query(Price).filter(Price.product_branch_id == product_branch.product_branch_id, Price.valid_to.is_(None)).one_or_none()
    )

    if current_price and current_price.amount == new_amount:
        return current_price

    now = datetime.now(timezone.utc)

    if current_price:
        current_price.valid_to = now

    new_price = Price(amount = new_amount, valid_from = now, valid_to = None, product_branch = product_branch)
    session.add(new_price)
    session.commit()
    session.refresh(new_price)
    return new_price

def delete_price(session: Session, product_sku: str, pc_branch: str):
    product_branch = get_one_product_branch(session, product_sku, pc_branch)

    if not product_branch:
        return None
    
    current_price = (
        session.query(Price).filter(Price.product_branch_id == product_branch.product_branch_id, Price.valid_to.is_(None)).one_or_none()
    )

    if not current_price:
        return None
    
    session.delete(current_price)
    session.commit()
    return True
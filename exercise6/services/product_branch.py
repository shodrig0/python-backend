from sqlalchemy.orm import Session
from models.product_branch import ProductBranch
from models.product import Product
from models.branch import Branch
from services.product import get_product_by_sku
from services.branch import get_branch_by_postal_code

def get_all_product_branch(session: Session):
    product_branch = session.query(ProductBranch).all()
    return product_branch

def group_products_branch(session: Session, sku_product: str, pc_branch: str, stock: int):
    product = get_product_by_sku(session, sku_product)
    branch = get_branch_by_postal_code(session, pc_branch)

    if not product:
        return None

    if not branch:
        return None
    
    existing = session.query(ProductBranch).filter_by(product_id = product.product_id, branch_id = branch.branch_id).first()

    if existing:
        raise ValueError("Relation already exists")

    product_branch = ProductBranch(product = product, branch = branch, stock = stock)

    session.add(product_branch)
    session.commit()
    session.refresh(product_branch)
    return product_branch

def get_one_product_branch(session: Session, sku_product: str, pc_branch: str):
    product_branch = (
        session.query(ProductBranch).join(ProductBranch.product).join(ProductBranch.branch).filter(Product.sku == sku_product, Branch.postal_code == pc_branch).first()
    )

    if not product_branch:
        return None

    return product_branch

def modify_stock_of_product(session: Session, sku_product: str, pc_branch: str, new_stock: int):
    product_branch = get_one_product_branch(session, sku_product, pc_branch)

    if not product_branch:
        return None
    
    if new_stock <= 0:
        raise ValueError("Invalid number")
    
    product_branch.stock = new_stock

    session.commit()
    session.refresh(product_branch)
    return product_branch

def delete_product_branch(session: Session, sku_product: str, pc_branch: str):
    product_branch = get_one_product_branch(session, sku_product, pc_branch)

    if not product_branch:
        raise None

    session.delete(product_branch)
    session.commit()
    return
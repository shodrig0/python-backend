from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.product_branch import ProductBranch
from models.product import Product
from models.branch import Branch

def get_all_product_branch(session: Session):
    product_branch = session.query(ProductBranch).all()

    if not product_branch:
        raise HTTPException(status_code = 404, detail = 'Not found')

    return product_branch

def group_products_branch(session: Session, sku_product: str, pc_branch: str, stock: int):
    product = session.query(Product).filter_by(sku = sku_product).first()
    branch = session.query(Branch).filter_by(postal_code = pc_branch).first()

    if not product:
        raise HTTPException(status_code = 404, detail = 'Product not found')

    if not branch:
        raise HTTPException(status_code = 404, detail = 'Branch not found')
    
    existing = session.query(ProductBranch).filter_by(product_id = product.product_id, branch_id = branch.branch_id).first()

    if existing:
        raise HTTPException(409, "Relation already exists")

    product_branch = ProductBranch(product = product, branch = branch, stock = stock)
    session.add(product_branch)
    session.commit()
    session.refresh(product_branch)
    return product_branch

def modify_stock_of_product(session: Session, sku_product: str, pc_branch: str, new_stock: int):
    product_branch = (
        session.query(ProductBranch).join(ProductBranch.product).join(ProductBranch.branch).filter(Product.sku == sku_product, Branch.postal_code == pc_branch).first()
    )

    if not product_branch:
        raise HTTPException(status_code = 404, detail = 'Product not found')
    
    if new_stock <= 0:
        raise HTTPException(status_code = 400, detail = 'Bad request')
    
    product_branch.stock = new_stock
    session.commit()
    session.refresh(product_branch)
    return product_branch
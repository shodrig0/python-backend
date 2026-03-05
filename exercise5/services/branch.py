from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.branch import Branch

def create_branch(session: Session, city: str, postal_code: str):
    branch = Branch(city = city, postal_code = postal_code)
    session.add(branch)
    return branch

def get_branches(session: Session):
    branches = session.query(Branch).all()

    if not branches:
        raise HTTPException(status_code = 404, detail = 'Branches not found')
    
    return branches

def get_branch_by_city(session: Session, city: str):
    branch = session.query(Branch).filter(Branch.city.ilike(f"{city}")).all()

    if not branch:
        raise HTTPException(status_code = 404, detail = 'Branch not found')
    
    return branch

def get_branch_by_postal_code(session: Session, postal_code: str):
    branch = session.query(Branch).filter_by(postal_code = postal_code).first()

    if not branch:
        raise HTTPException(status_code = 404, detail = 'Branch not found')
    
    return branch

def update_branch_postal_code(session: Session, city: str, new_postal_code: str):
    branch = session.query(Branch).filter_by(city = city).first()
    
    if not branch:
        raise HTTPException(status_code = 404, detail = 'Branch not found')
    
    branch.postal_code = new_postal_code
    return branch

def delete_branch_by_postal_code(session: Session, postal_code: str):
    branch = session.query(Branch).filter_by(postal_code = postal_code).first()

    if not branch:
        return None
    
    session.delete(branch)
    return True
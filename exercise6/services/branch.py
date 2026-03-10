from sqlalchemy.orm import Session
from models.branch import Branch

def create_branch(session: Session, city: str, postal_code: str):
    branch = Branch(city = city, postal_code = postal_code)
    session.add(branch)
    session.commit()
    session.refresh(branch)
    return branch

def get_branches(session: Session):
    branches = session.query(Branch).all()
    return branches

def get_branch_by_postal_code(session: Session, postal_code: str):
    branch = session.query(Branch).filter(Branch.postal_code.ilike(f"%{postal_code}%")).first()

    if not branch:
        return None
    
    return branch

def modify_city_of_branch_by_postal_code(session: Session, postal_code: str, branch_data: dict):
    branch = get_branch_by_postal_code(session, postal_code)

    if "city" in branch_data:
        branch.city = branch_data["city"]

    session.commit()
    session.refresh(branch)
    return branch

def delete_branch_by_postal_code(session: Session, postal_code: str):
    branch = session.query(Branch).filter_by(postal_code = postal_code).first()

    if not branch:
        return None

    session.delete(branch)
    session.commit()
    return True
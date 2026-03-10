from sqlalchemy.orm import Session
from models.category import Category

def create_category(session: Session, category_data: dict):
    category = Category(name = category_data["name"])
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_all_categories(session: Session):
    categories = session.query(Category).all()
    return categories

def get_category_by_name(session: Session, name: str):
    category = session.query(Category).filter(Category.name.ilike(f"{name}")).first()
    
    if not category:
        return None

    return category

def modify_category_name(session: Session, name: str, update_data: dict):
    category = get_category_by_name(session, name)

    if not category:
        return None

    if "name" in update_data:
        category.name = update_data["name"]

    session.commit()
    session.refresh(category)
    return category

def delete_category_by_name(session: Session, name: str):
    category = get_category_by_name(session, name)

    if not category:
        return None

    session.delete(category)
    session.commit()
    return True
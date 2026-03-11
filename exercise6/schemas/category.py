from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from services.initializer import get_session
from services.category import create_category, get_all_categories, delete_category_by_name, modify_category_name

category_router = APIRouter()

class CategoryResponse(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes = True)

class CategoryCreate(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes = True)

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

    model_config = ConfigDict(from_attributes = True)

@category_router.post('/categories')
async def create_categories(category: CategoryCreate, session: Session = Depends(get_session)):
    category = create_category(session, category.name)

    if not category:
        raise HTTPException(status_code = 400, detail = 'Bad request')

    return category

@category_router.get('/categories')
async def read_categories(session: Session = Depends(get_session)):
    return get_all_categories(session)

@category_router.get('/categories/{name}')
async def read_category_by_name():
    return

@category_router.patch('/categories/{name}')
async def update_category_name(name: str, category_model: CategoryUpdate, session: Session = Depends(get_session)):
    category_update = category_model.model_dump(exclude_unset = True)
    category = modify_category_name(session, name, category_update)

    if not category:
        raise HTTPException(status_code = 404, detail = 'category not found')

    return category

@category_router.delete('/categories/{name}')
async def delete_category(name: str, session: Session = Depends(get_session)):
    category = delete_category_by_name(session, name)

    if not category:
        raise HTTPException(status_code = 404, detail = 'category not found')
    
    return { "detail": "Category deleted successfully" }
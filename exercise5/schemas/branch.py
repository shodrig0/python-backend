from pydantic import BaseModel, ConfigDict
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from services.initializer import get_session
from services.branch import get_branches, get_branch_by_city, get_branch_by_postal_code

branch_router = APIRouter()

class BranchResponse(BaseModel):
    city: str
    postal_code: str

    model_config = ConfigDict(from_attributes = True)

class BranchUpdate(BaseModel):
    city: Optional[str] = None
    postal_code: Optional[str] = None

    model_config = ConfigDict(from_attributes = True)

@branch_router.get('/branches')
async def read_branches(session: Session = Depends(get_session)):
    return get_branches(session)

@branch_router.get('/branches/{city}')
async def read_branch_by_city(city: str, session: Session = Depends(get_session)):
    branch = get_branch_by_city(session, city)

    if not branch:
        raise HTTPException(status_code = 404, detail = 'Branch not found')

    return branch
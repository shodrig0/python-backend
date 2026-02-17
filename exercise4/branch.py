from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Optional
from data import branchs

branch_router = APIRouter()

class Branch(BaseModel):
    id: int
    name: str
    region: str
    postal_code: str

class BranchUpdate(BaseModel):
    name: Optional[str] = None
    region: Optional[str] = None
    postal_code: Optional[str] = None

@branch_router.get("/branch")
async def get_branch(name: str | None = None):
    data_list = branchs
    if name is not None:
        new_list = []
        for b in data_list:
            if name.lower() in b["name"].lower():
                new_list.append(b)
        data_list = new_list
    return data_list

@branch_router.get("/branch/{id}")
async def get_branch_by_id(id: int):
    for branch in branchs:
        if branch["id"] == id:
            return branch
    raise HTTPException(status_code = 404, detail = "No data")

@branch_router.post("/branch")
async def create_branch(branch: Branch):
    branchs.append(branch.model_dump())
    return branch

@branch_router.put("/branch/{id}")
async def update_branch_by_id(id: int, branch: Branch):
    for branch_id, b in enumerate(branchs):
        if b["id"] == id:
            branchs[branch_id] = branch.model_dump()
            return branchs[branch_id]
    raise HTTPException(status_code = 404, detail = "No data")

@branch_router.patch("/branch/{id}")
async def partial_update_branch_by_id(id: int, branch: BranchUpdate):
    for branch_id, b in enumerate(branchs):
        if b["id"] == id:
            update_data_branch = branch.model_dump(exclude_unset = True)
            b.update(update_data_branch)
            return branchs[branch_id]
    raise HTTPException(status_code = 404, detail = "No data")

@branch_router.delete("/branch/{id}")
async def delete_branch_by_id(id: int):
    for branch_id, b in enumerate(branchs):
        if b["id"] == id:
            branchs.pop(branch_id)
            return { "msg": "Successfully removed" }
    raise HTTPException(status_code = 404, detail = "No data")
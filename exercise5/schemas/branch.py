from pydantic import BaseModel, ConfigDict

class BranchResponse(BaseModel):
    branch_id: int
    city: str
    postal_code: str

    model_config = ConfigDict(from_attributes = True)
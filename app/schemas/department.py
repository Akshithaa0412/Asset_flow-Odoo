from pydantic import BaseModel
from typing import Optional


class DepartmentCreate(BaseModel):
    department_name: str
    parent_department_id: Optional[int] = None


class DepartmentUpdate(BaseModel):
    department_name: str


class DepartmentResponse(BaseModel):
    department_id: int
    department_name: str
    status: str

    class Config:
        from_attributes = True
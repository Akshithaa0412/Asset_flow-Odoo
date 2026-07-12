from pydantic import BaseModel
from typing import Optional


class EmployeeUpdate(BaseModel):
    employee_name: str
    phone: Optional[str] = None
    department_id: Optional[int] = None
    designation: Optional[str] = None


class StatusUpdate(BaseModel):
    status: str


class EmployeeResponse(BaseModel):
    employee_id: int
    user_id: int
    employee_name: str
    phone: Optional[str]
    department_id: Optional[int]
    designation: Optional[str]
    status: str

    class Config:
        from_attributes = True
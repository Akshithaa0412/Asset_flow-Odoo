from datetime import datetime
from pydantic import BaseModel

from app.models.allocation import AllocationStatus


class AllocationCreate(BaseModel):
    asset_id: int
    employee_id: int
    allocated_by: int
    expected_return_date: datetime | None = None


class AllocationResponse(BaseModel):
    allocation_id: int
    asset_id: int
    employee_id: int
    allocated_by: int
    status: AllocationStatus

    class Config:
        from_attributes = True

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.allocation import AllocationStatus


class AllocationCreate(BaseModel):
    asset_id: int = Field(gt=0)
    employee_id: int = Field(gt=0)
    expected_return_date: Optional[datetime] = None


class AllocationReturn(BaseModel):
    checkin_notes: Optional[str] = Field(
        default=None,
        max_length=500,
    )


class AllocationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    allocation_id: int
    asset_id: int
    employee_id: int
    allocated_by: int
    allocated_at: datetime
    expected_return_date: Optional[datetime]
    returned_at: Optional[datetime]
    status: AllocationStatus
    checkin_notes: Optional[str]

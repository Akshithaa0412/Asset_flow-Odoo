from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.maintenance_request import MaintenanceStatus


class MaintenanceCreate(BaseModel):
    asset_id: int = Field(gt=0)
    issue_description: str = Field(min_length=5)


class MaintenanceDecision(BaseModel):
    reason: Optional[str] = Field(default=None, max_length=500)


class MaintenanceComplete(BaseModel):
    resolution_notes: str = Field(min_length=3)


class MaintenanceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    maintenance_id: int
    asset_id: int
    requested_by: int
    approved_by: Optional[int]
    issue_description: str
    status: MaintenanceStatus
    resolution_notes: Optional[str]
    requested_at: datetime
    approved_at: Optional[datetime]
    completed_at: Optional[datetime]

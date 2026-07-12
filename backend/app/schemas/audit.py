from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.audit import AuditItemStatus, AuditStatus


class AuditCycleCreate(BaseModel):
    name: str = Field(min_length=3, max_length=150)


class AuditItemCreate(BaseModel):
    asset_id: int = Field(gt=0)


class AuditItemUpdate(BaseModel):
    status: AuditItemStatus
    notes: Optional[str] = Field(default=None, max_length=500)


class AuditCycleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    audit_id: int
    name: str
    created_by: int
    status: AuditStatus
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime


class AuditItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    audit_item_id: int
    audit_id: int
    asset_id: int
    status: AuditItemStatus
    notes: Optional[str]
    verified_at: Optional[datetime]

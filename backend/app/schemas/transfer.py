from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.models.transfer import TransferStatus


class TransferCreate(BaseModel):
    asset_id: int = Field(gt=0)
    to_employee_id: int = Field(gt=0)
    reason: Optional[str] = Field(default=None, max_length=500)


class TransferDecision(BaseModel):
    reason: Optional[str] = Field(default=None, max_length=500)


class TransferResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    transfer_id: int
    asset_id: int
    from_employee_id: int
    to_employee_id: int
    requested_by: int
    approved_by: Optional[int]
    status: TransferStatus
    reason: Optional[str]
    requested_at: datetime
    reviewed_at: Optional[datetime]

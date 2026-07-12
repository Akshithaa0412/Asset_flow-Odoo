from datetime import date
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AssetBase(BaseModel):
    asset_code: str
    name: str
    description: str | None = None
    serial_number: str | None = None
    category_id: UUID
    vendor_id: UUID
    department_id: UUID
    purchase_date: date | None = None
    purchase_cost: Decimal | None = None
    warranty_expiry: date | None = None
    status: str = "AVAILABLE"
    asset_condition: str = "GOOD"
    location: str | None = None


class AssetCreate(AssetBase):
    pass


class AssetUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: str | None = None
    asset_condition: str | None = None
    location: str | None = None


class AssetResponse(AssetBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
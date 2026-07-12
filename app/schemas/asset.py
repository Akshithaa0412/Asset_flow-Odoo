from pydantic import BaseModel
from typing import Optional
from datetime import date


class AssetCreate(BaseModel):
    asset_name: str
    category_id: int
    serial_number: Optional[str] = None
    acquisition_date: Optional[date] = None
    acquisition_cost: Optional[float] = None
    asset_condition: Optional[str] = None
    location: Optional[str] = None
    is_bookable: bool = False
    department_id: Optional[int] = None
    image_url: Optional[str] = None


class AssetUpdate(BaseModel):
    asset_name: str
    category_id: int
    serial_number: Optional[str] = None
    acquisition_date: Optional[date] = None
    acquisition_cost: Optional[float] = None
    asset_condition: Optional[str] = None
    location: Optional[str] = None
    asset_status: str
    is_bookable: bool
    department_id: Optional[int] = None
    image_url: Optional[str] = None


class AssetResponse(BaseModel):
    asset_id: int
    asset_tag: str
    asset_name: str
    category_id: int
    serial_number: Optional[str]
    acquisition_date: Optional[date]
    acquisition_cost: Optional[float]
    asset_condition: Optional[str]
    location: Optional[str]
    asset_status: str
    is_bookable: bool
    department_id: Optional[int]
    image_url: Optional[str]

    class Config:
        from_attributes = True
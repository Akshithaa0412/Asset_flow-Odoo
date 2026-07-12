from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.asset import AssetCreate, AssetResponse
from app.services.asset_service import AssetService

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.get("/", response_model=list[AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    return AssetService.get_assets(db)


@router.get("/{asset_id}", response_model=AssetResponse)
def get_asset(asset_id: UUID, db: Session = Depends(get_db)):
    return AssetService.get_asset(db, asset_id)


@router.post("/", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    return AssetService.create_asset(db, asset)
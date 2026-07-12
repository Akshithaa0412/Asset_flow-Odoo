from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.database.session import get_db
from app.services.asset_service import (
    search_assets
)
from app.schemas.asset import (
    AssetCreate,
    AssetUpdate,
    AssetResponse
)

from app.services.asset_service import (
    get_all_assets,
    get_asset,
    create_asset,
    update_asset,
    delete_asset
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.get("/", response_model=list[AssetResponse])
def get_assets(db: Session = Depends(get_db)):
    return get_all_assets(db)

@router.get("/search/", response_model=list[AssetResponse])
def search(
    asset_tag: Optional[str] = None,
    asset_name: Optional[str] = None,
    category_id: Optional[int] = None,
    status: Optional[str] = None,
    department_id: Optional[int] = None,
    location: Optional[str] = None,
    db: Session = Depends(get_db)
):

    return search_assets(
        db,
        asset_tag,
        asset_name,
        category_id,
        status,
        department_id,
        location,
    )
@router.get("/{asset_id}", response_model=AssetResponse)
def get_one(asset_id: int, db: Session = Depends(get_db)):
    asset = get_asset(db, asset_id)

    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")

    return asset


@router.post("/", response_model=AssetResponse)
def create(request: AssetCreate, db: Session = Depends(get_db)):
    return create_asset(db, request)


@router.put("/{asset_id}", response_model=AssetResponse)
def update(asset_id: int, request: AssetUpdate, db: Session = Depends(get_db)):
    asset = update_asset(db, asset_id, request)

    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")

    return asset


@router.delete("/{asset_id}")
def delete(asset_id: int, db: Session = Depends(get_db)):
    deleted = delete_asset(db, asset_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Asset not found")

    return {
        "message": "Asset deleted successfully"
    }

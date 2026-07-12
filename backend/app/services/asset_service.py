from sqlalchemy.orm import Session

from app.repositories.asset_repository import AssetRepository
from app.schemas.asset import AssetCreate


class AssetService:

    @staticmethod
    def get_assets(db: Session):
        return AssetRepository.get_all(db)

    @staticmethod
    def get_asset(db: Session, asset_id):
        return AssetRepository.get_by_id(db, asset_id)

    @staticmethod
    def create_asset(db: Session, asset: AssetCreate):
        return AssetRepository.create(db, asset)
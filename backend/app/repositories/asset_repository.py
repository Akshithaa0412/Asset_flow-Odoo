from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.schemas.asset import AssetCreate


class AssetRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Asset).all()

    @staticmethod
    def get_by_id(db: Session, asset_id):
        return db.query(Asset).filter(Asset.id == asset_id).first()

    @staticmethod
    def create(db: Session, asset: AssetCreate):
        new_asset = Asset(**asset.model_dump())

        db.add(new_asset)
        db.commit()
        db.refresh(new_asset)

        return new_asset
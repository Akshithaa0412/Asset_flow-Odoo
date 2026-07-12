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
    
    @staticmethod
    def update(db: Session, asset_id, asset_data):
        asset = db.query(Asset).filter(Asset.id == asset_id).first()

        if not asset:
            return None

        for key, value in asset_data.model_dump(exclude_unset=True).items():
            setattr(asset, key, value)

        db.commit()
        db.refresh(asset)

        return asset


    @staticmethod
    def delete(db: Session, asset_id):
        asset = db.query(Asset).filter(Asset.id == asset_id).first()

        if not asset:
            return None

        db.delete(asset)
        db.commit()

        return asset
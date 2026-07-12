from sqlalchemy.orm import Session
from app.models.asset import Asset


def generate_asset_tag(db: Session):
    count = db.query(Asset).count() + 1
    return f"AF-{count:04d}"


def get_all_assets(db: Session):
    return db.query(Asset).all()


def get_asset(db: Session, asset_id: int):
    return db.query(Asset).filter(
        Asset.asset_id == asset_id
    ).first()


def create_asset(db: Session, data):

    asset = Asset(
        asset_tag=generate_asset_tag(db),
        asset_name=data.asset_name,
        category_id=data.category_id,
        serial_number=data.serial_number,
        acquisition_date=data.acquisition_date,
        acquisition_cost=data.acquisition_cost,
        asset_condition=data.asset_condition,
        location=data.location,
        asset_status="Available",
        is_bookable=data.is_bookable,
        department_id=data.department_id,
        image_url=data.image_url
    )

    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset


def update_asset(db: Session, asset_id: int, data):

    asset = db.query(Asset).filter(
        Asset.asset_id == asset_id
    ).first()

    if asset is None:
        return None

    asset.asset_name = data.asset_name
    asset.category_id = data.category_id
    asset.serial_number = data.serial_number
    asset.acquisition_date = data.acquisition_date
    asset.acquisition_cost = data.acquisition_cost
    asset.asset_condition = data.asset_condition
    asset.location = data.location
    asset.asset_status = data.asset_status
    asset.is_bookable = data.is_bookable
    asset.department_id = data.department_id
    asset.image_url = data.image_url

    db.commit()
    db.refresh(asset)

    return asset


def delete_asset(db: Session, asset_id: int):

    asset = db.query(Asset).filter(
        Asset.asset_id == asset_id
    ).first()

    if asset is None:
        return False

    db.delete(asset)
    db.commit()

    return True
from sqlalchemy import or_


def search_assets(
    db: Session,
    asset_tag=None,
    asset_name=None,
    category_id=None,
    status=None,
    department_id=None,
    location=None,
):

    query = db.query(Asset)

    if asset_tag:
        query = query.filter(Asset.asset_tag.ilike(f"%{asset_tag}%"))

    if asset_name:
        query = query.filter(Asset.asset_name.ilike(f"%{asset_name}%"))

    if category_id:
        query = query.filter(Asset.category_id == category_id)

    if status:
        query = query.filter(Asset.asset_status == status)

    if department_id:
        query = query.filter(Asset.department_id == department_id)

    if location:
        query = query.filter(Asset.location.ilike(f"%{location}%"))

    return query.all()
from sqlalchemy.orm import Session

from app.models.asset_category import AssetCategory


def get_all_categories(db: Session):
    return db.query(AssetCategory).all()


def get_category(db: Session, category_id: int):
    return db.query(AssetCategory).filter(
        AssetCategory.category_id == category_id
    ).first()


def create_category(db: Session, data):
    category = AssetCategory(
        category_name=data.category_name,
        description=data.description,
        status="Active"
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def update_category(db: Session, category_id: int, data):

    category = db.query(AssetCategory).filter(
        AssetCategory.category_id == category_id
    ).first()

    if category is None:
        return None

    category.category_name = data.category_name
    category.description = data.description
    category.status = data.status

    db.commit()
    db.refresh(category)

    return category


def delete_category(db: Session, category_id: int):

    category = db.query(AssetCategory).filter(
        AssetCategory.category_id == category_id
    ).first()

    if category is None:
        return False

    db.delete(category)
    db.commit()

    return True
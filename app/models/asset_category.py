from sqlalchemy import Column, Integer, String

from app.database.base import Base


class AssetCategory(Base):
    __tablename__ = "asset_categories"

    category_id = Column(Integer, primary_key=True)

    category_name = Column(String(100), unique=True)

    description = Column(String)

    status = Column(String(20), default="Active")
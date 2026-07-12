from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Numeric,
    Date,
    ForeignKey,
    DateTime,
)
from sqlalchemy.sql import func

from app.database.base import Base


class Asset(Base):
    __tablename__ = "assets"

    asset_id = Column(Integer, primary_key=True)

    asset_tag = Column(String(20), unique=True, nullable=False)

    asset_name = Column(String(150), nullable=False)

    category_id = Column(
        Integer,
        ForeignKey("asset_categories.category_id")
    )

    serial_number = Column(String(100), unique=True)

    acquisition_date = Column(Date)

    acquisition_cost = Column(Numeric(12, 2))

    asset_condition = Column(String(20))

    location = Column(String(150))

    asset_status = Column(String(30), default="Available")

    is_bookable = Column(Boolean, default=False)

    image_url = Column(String)

    department_id = Column(
        Integer,
        ForeignKey("departments.department_id")
    )

    created_at = Column(DateTime, server_default=func.now())
import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Date,
    DateTime,
    ForeignKey,
    Numeric
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    asset_code = Column(String(30), unique=True, nullable=False)

    name = Column(String(150), nullable=False)

    description = Column(Text)

    serial_number = Column(String(100), unique=True)

    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("categories.id"),
        nullable=False
    )

    vendor_id = Column(
        UUID(as_uuid=True),
        ForeignKey("vendors.id"),
        nullable=False
    )

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )

    purchase_date = Column(Date)

    purchase_cost = Column(Numeric(12, 2))

    warranty_expiry = Column(Date)

    status = Column(String(20), default="AVAILABLE")

    asset_condition = Column(String(20), default="GOOD")

    location = Column(String(150))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    category = relationship(
        "Category",
        back_populates="assets"
    )

    vendor = relationship(
        "Vendor",
        back_populates="assets"
    )

    department = relationship(
        "Department",
        back_populates="assets"
    )

    bookings = relationship(
        "Booking",
        back_populates="asset",
        cascade="all, delete-orphan"
    )

    maintenance_records = relationship(
        "Maintenance",
        back_populates="asset",
        cascade="all, delete-orphan"
    )
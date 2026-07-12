import uuid

from sqlalchemy import Column, Date, Numeric, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    asset_id = Column(
        UUID(as_uuid=True),
        ForeignKey("assets.id"),
        nullable=False
    )

    issue = Column(Text, nullable=False)

    priority = Column(String(20))

    assigned_to = Column(String(100))

    reported_date = Column(Date)

    completed_date = Column(Date)

    cost = Column(Numeric(10, 2))

    status = Column(String(20))

    asset = relationship(
        "Asset",
        back_populates="maintenance_records"
    )
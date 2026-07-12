from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from sqlalchemy.orm import relationship
from app.db.database import Base


class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(150), nullable=False)

    email = Column(String(100))

    phone = Column(String(20))

    address = Column(Text)
    assets = relationship(
    "Asset",
    back_populates="vendor"
)
    website = Column(String(255))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
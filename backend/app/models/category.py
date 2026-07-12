from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from sqlalchemy.orm import relationship

from app.db.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String(100), unique=True, nullable=False)

    description = Column(Text)
    assets = relationship(
    "Asset",
    back_populates="category"
)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
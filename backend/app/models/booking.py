import uuid

from sqlalchemy import Column, Date, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    asset_id = Column(
        UUID(as_uuid=True),
        ForeignKey("assets.id"),
        nullable=False
    )

    employee_id = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id"),
        nullable=False
    )

    issue_date = Column(Date, nullable=False)

    expected_return = Column(Date)

    actual_return = Column(Date)

    approved_by = Column(String(100))

    status = Column(String(20))

    remarks = Column(Text)

    asset = relationship(
        "Asset",
        back_populates="bookings"
    )

    employee = relationship(
        "Employee",
        back_populates="bookings"
    )
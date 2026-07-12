import uuid

from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    employee_code = Column(String(20), unique=True, nullable=False)

    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50))

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(20))

    designation = Column(String(100))

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )

    joining_date = Column(Date)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )
    bookings = relationship(
    "Booking",
    back_populates="employee"
)
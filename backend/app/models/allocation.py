import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Integer, String

from app.database import Base


class AllocationStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class Allocation(Base):
    __tablename__ = "allocations"

    allocation_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    asset_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    employee_id = Column(
        Integer,
        nullable=False,
        index=True,
    )

    allocated_by = Column(
        Integer,
        nullable=False,
    )

    allocated_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    expected_return_date = Column(
        DateTime,
        nullable=True,
    )

    returned_at = Column(
        DateTime,
        nullable=True,
    )

    status = Column(
        Enum(AllocationStatus),
        default=AllocationStatus.ACTIVE,
        nullable=False,
    )

    checkin_notes = Column(
        String(500),
        nullable=True,
    )

import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String

# Temporary import until Member 1's shared Base is available.
# Later we will replace this with:
# from app.database.base import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AllocationStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


class Allocation(Base):
    __tablename__ = "allocations"

    allocation_id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(
        Integer,
        ForeignKey("assets.asset_id"),
        nullable=False,
        index=True,
    )

    employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False,
        index=True,
    )

    allocated_by = Column(
        Integer,
        ForeignKey("users.user_id"),
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

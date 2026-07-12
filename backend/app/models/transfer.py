import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String

# Temporary until Member 1's shared Base is ready
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TransferStatus(str, enum.Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class Transfer(Base):
    __tablename__ = "transfers"

    transfer_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    asset_id = Column(
        Integer,
        ForeignKey("assets.asset_id"),
        nullable=False,
        index=True,
    )

    from_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False,
    )

    to_employee_id = Column(
        Integer,
        ForeignKey("employees.employee_id"),
        nullable=False,
    )

    requested_by = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
    )

    approved_by = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=True,
    )

    status = Column(
        Enum(TransferStatus),
        default=TransferStatus.REQUESTED,
        nullable=False,
    )

    reason = Column(
        String(500),
        nullable=True,
    )

    requested_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    reviewed_at = Column(
        DateTime,
        nullable=True,
    )

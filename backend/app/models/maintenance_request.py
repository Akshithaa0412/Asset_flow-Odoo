import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base

# Temporary until Member 1 provides the shared Base
Base = declarative_base()


class MaintenanceStatus(str, enum.Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class MaintenanceRequest(Base):
    __tablename__ = "maintenance_requests"

    maintenance_id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(
        Integer,
        ForeignKey("assets.asset_id"),
        nullable=False,
        index=True,
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

    issue_description = Column(
        Text,
        nullable=False,
    )

    status = Column(
        Enum(MaintenanceStatus),
        default=MaintenanceStatus.REQUESTED,
        nullable=False,
    )

    resolution_notes = Column(
        Text,
        nullable=True,
    )

    requested_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    approved_at = Column(
        DateTime,
        nullable=True,
    )

    completed_at = Column(
        DateTime,
        nullable=True,
    )

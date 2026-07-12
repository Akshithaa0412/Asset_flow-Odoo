import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

# Temporary until Member 1 provides the shared Base
Base = declarative_base()


class AuditStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"


class AuditItemStatus(str, enum.Enum):
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    MISSING = "MISSING"
    DAMAGED = "DAMAGED"


class AuditCycle(Base):
    __tablename__ = "audit_cycles"

    audit_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    created_by = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
    )

    status = Column(
        Enum(AuditStatus),
        default=AuditStatus.DRAFT,
        nullable=False,
    )

    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


class AuditItem(Base):
    __tablename__ = "audit_items"

    audit_item_id = Column(Integer, primary_key=True, index=True)

    audit_id = Column(
        Integer,
        ForeignKey("audit_cycles.audit_id"),
        nullable=False,
        index=True,
    )

    asset_id = Column(
        Integer,
        ForeignKey("assets.asset_id"),
        nullable=False,
    )

    status = Column(
        Enum(AuditItemStatus),
        default=AuditItemStatus.PENDING,
        nullable=False,
    )

    notes = Column(String(500), nullable=True)

    verified_at = Column(DateTime, nullable=True)

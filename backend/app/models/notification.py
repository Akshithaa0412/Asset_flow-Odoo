import enum
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import declarative_base

# Temporary until the shared Base is available
Base = declarative_base()


class NotificationType(str, enum.Enum):
    ALLOCATION = "ALLOCATION"
    TRANSFER = "TRANSFER"
    BOOKING = "BOOKING"
    MAINTENANCE = "MAINTENANCE"
    AUDIT = "AUDIT"
    SYSTEM = "SYSTEM"


class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
        index=True,
    )

    notification_type = Column(
        Enum(NotificationType),
        nullable=False,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    message = Column(
        Text,
        nullable=False,
    )

    is_read = Column(
        Boolean,
        default=False,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

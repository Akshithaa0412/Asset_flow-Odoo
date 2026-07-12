import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer

# Temporary until Member 1's shared Base is ready
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BookingStatus(str, enum.Enum):
    UPCOMING = "UPCOMING"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(
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

    booked_by = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False,
    )

    start_time = Column(
        DateTime,
        nullable=False,
        index=True,
    )

    end_time = Column(
        DateTime,
        nullable=False,
        index=True,
    )

    status = Column(
        Enum(BookingStatus),
        default=BookingStatus.UPCOMING,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

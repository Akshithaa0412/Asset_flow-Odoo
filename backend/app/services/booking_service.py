from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.booking import Booking, BookingStatus
from app.models.notification import NotificationType
from app.services.notification_service import NotificationService


class BookingService:
    @staticmethod
    def create_booking(
        db: Session,
        asset,
        booked_by: int,
        start_time,
        end_time,
    ) -> Booking:

        # Rule 1: Only bookable assets can be booked
        if not asset.is_bookable:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This asset is not available for booking.",
            )

        # Rule 2: Prevent overlapping bookings
        overlapping_booking = (
            db.query(Booking)
            .filter(
                Booking.asset_id == asset.asset_id,
                Booking.status.in_(
                    [
                        BookingStatus.UPCOMING,
                        BookingStatus.ONGOING,
                    ]
                ),
                Booking.start_time < end_time,
                Booking.end_time > start_time,
            )
            .first()
        )

        if overlapping_booking:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This asset is already booked for the selected time.",
            )

        booking = Booking(
            asset_id=asset.asset_id,
            booked_by=booked_by,
            start_time=start_time,
            end_time=end_time,
            status=BookingStatus.UPCOMING,
        )

        db.add(booking)

        NotificationService.create_notification(
            db=db,
            user_id=booked_by,
            notification_type=NotificationType.BOOKING,
            title="Booking Confirmed",
            message=f"Your booking for asset {asset.asset_tag} has been confirmed.",
        )

        try:
            db.commit()
            db.refresh(booking)
            return booking

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def cancel_booking(
        db: Session,
        booking: Booking,
    ) -> Booking:

        if booking.status in [
            BookingStatus.COMPLETED,
            BookingStatus.CANCELLED,
        ]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This booking cannot be cancelled.",
            )

        booking.status = BookingStatus.CANCELLED

        try:
            db.commit()
            db.refresh(booking)
            return booking

        except Exception:
            db.rollback()
            raise

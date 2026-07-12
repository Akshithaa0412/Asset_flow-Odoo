from sqlalchemy.orm import Session

from app.models.notification import Notification, NotificationType


class NotificationService:
    @staticmethod
    def create_notification(
        db: Session,
        user_id: int,
        notification_type: NotificationType,
        title: str,
        message: str,
    ) -> Notification:
        notification = Notification(
            user_id=user_id,
            notification_type=notification_type,
            title=title,
            message=message,
        )

        db.add(notification)

        # Important:
        # We do NOT commit here.
        # The main workflow service will commit the entire transaction.

        return notification

    @staticmethod
    def mark_as_read(
        db: Session,
        notification: Notification,
    ) -> Notification:
        notification.is_read = True
        db.flush()
        return notification

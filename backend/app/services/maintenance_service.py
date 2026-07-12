from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.maintenance_request import (
    MaintenanceRequest,
    MaintenanceStatus,
)
from app.models.notification import NotificationType
from app.services.notification_service import NotificationService


class MaintenanceService:
    @staticmethod
    def create_request(
        db: Session,
        asset_id: int,
        requested_by: int,
        issue_description: str,
    ) -> MaintenanceRequest:

        maintenance = MaintenanceRequest(
            asset_id=asset_id,
            requested_by=requested_by,
            issue_description=issue_description,
            status=MaintenanceStatus.REQUESTED,
        )

        db.add(maintenance)

        NotificationService.create_notification(
            db=db,
            user_id=requested_by,
            notification_type=NotificationType.MAINTENANCE,
            title="Maintenance Request Created",
            message=f"Maintenance request created for asset {asset_id}.",
        )

        try:
            db.commit()
            db.refresh(maintenance)
            return maintenance

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def approve_request(
        db: Session,
        maintenance: MaintenanceRequest,
        approved_by: int,
    ) -> MaintenanceRequest:

        if maintenance.status != MaintenanceStatus.REQUESTED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only requested maintenance can be approved.",
            )

        maintenance.status = MaintenanceStatus.APPROVED
        maintenance.approved_by = approved_by
        maintenance.approved_at = datetime.utcnow()

        NotificationService.create_notification(
            db=db,
            user_id=maintenance.requested_by,
            notification_type=NotificationType.MAINTENANCE,
            title="Maintenance Approved",
            message="Your maintenance request has been approved.",
        )

        try:
            db.commit()
            db.refresh(maintenance)
            return maintenance

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def start_maintenance(
        db: Session,
        maintenance: MaintenanceRequest,
    ) -> MaintenanceRequest:

        if maintenance.status != MaintenanceStatus.APPROVED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only approved maintenance can start.",
            )

        maintenance.status = MaintenanceStatus.IN_PROGRESS

        try:
            db.commit()
            db.refresh(maintenance)
            return maintenance

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def complete_request(
        db: Session,
        maintenance: MaintenanceRequest,
        resolution_notes: str,
    ) -> MaintenanceRequest:

        if maintenance.status != MaintenanceStatus.IN_PROGRESS:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only ongoing maintenance can be completed.",
            )

        maintenance.status = MaintenanceStatus.COMPLETED
        maintenance.resolution_notes = resolution_notes
        maintenance.completed_at = datetime.utcnow()

        NotificationService.create_notification(
            db=db,
            user_id=maintenance.requested_by,
            notification_type=NotificationType.MAINTENANCE,
            title="Maintenance Completed",
            message="Your maintenance request has been completed.",
        )

        try:
            db.commit()
            db.refresh(maintenance)
            return maintenance

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def reject_request(
        db: Session,
        maintenance: MaintenanceRequest,
    ) -> MaintenanceRequest:

        if maintenance.status != MaintenanceStatus.REQUESTED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only requested maintenance can be rejected.",
            )

        maintenance.status = MaintenanceStatus.REJECTED

        try:
            db.commit()
            db.refresh(maintenance)
            return maintenance

        except Exception:
            db.rollback()
            raise

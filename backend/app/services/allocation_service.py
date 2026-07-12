from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.allocation import Allocation, AllocationStatus
from app.models.notification import NotificationType
from app.services.notification_service import NotificationService


class AllocationService:
    @staticmethod
    def allocate_asset(
        db: Session,
        asset,
        employee,
        allocated_by: int,
        expected_return_date=None,
    ) -> Allocation:

        # Rule 1: Prevent double allocation
        existing_allocation = (
            db.query(Allocation)
            .filter(
                Allocation.asset_id == asset.asset_id,
                Allocation.status == AllocationStatus.ACTIVE,
            )
            .first()
        )

        if existing_allocation:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Asset is already allocated.",
            )

        # Rule 2: Asset must be available
        if asset.asset_status != "Available":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only available assets can be allocated.",
            )

        allocation = Allocation(
            asset_id=asset.asset_id,
            employee_id=employee.employee_id,
            allocated_by=allocated_by,
            expected_return_date=expected_return_date,
            status=AllocationStatus.ACTIVE,
        )

        db.add(allocation)

        # Automatically update asset status
        asset.asset_status = "Allocated"

        # Generate notification for employee's user account
        NotificationService.create_notification(
            db=db,
            user_id=employee.user_id,
            notification_type=NotificationType.ALLOCATION,
            title="Asset Allocated",
            message=f"Asset {asset.asset_tag} has been allocated to you.",
        )

        try:
            db.commit()
            db.refresh(allocation)
            return allocation

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def return_asset(
        db: Session,
        allocation: Allocation,
        asset,
        employee,
        checkin_notes=None,
    ) -> Allocation:

        if allocation.status != AllocationStatus.ACTIVE:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This allocation is not active.",
            )

        allocation.status = AllocationStatus.RETURNED
        allocation.returned_at = datetime.utcnow()
        allocation.checkin_notes = checkin_notes

        # Asset becomes available again
        asset.asset_status = "Available"

        NotificationService.create_notification(
            db=db,
            user_id=employee.user_id,
            notification_type=NotificationType.ALLOCATION,
            title="Asset Returned",
            message=f"Asset {asset.asset_tag} has been returned successfully.",
        )

        try:
            db.commit()
            db.refresh(allocation)
            return allocation

        except Exception:
            db.rollback()
            raise

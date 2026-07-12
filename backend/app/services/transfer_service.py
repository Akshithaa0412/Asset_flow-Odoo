from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.allocation import Allocation, AllocationStatus
from app.models.notification import NotificationType
from app.models.transfer import Transfer, TransferStatus
from app.services.notification_service import NotificationService


class TransferService:
    @staticmethod
    def request_transfer(
        db: Session,
        asset,
        from_employee,
        to_employee,
        requested_by: int,
        reason=None,
    ) -> Transfer:

        if from_employee.employee_id == to_employee.employee_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Asset cannot be transferred to the same employee.",
            )

        # The asset must currently belong to the source employee
        active_allocation = (
            db.query(Allocation)
            .filter(
                Allocation.asset_id == asset.asset_id,
                Allocation.employee_id == from_employee.employee_id,
                Allocation.status == AllocationStatus.ACTIVE,
            )
            .first()
        )

        if not active_allocation:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Source employee does not have an active allocation for this asset.",
            )

        # Prevent multiple pending transfer requests
        existing_transfer = (
            db.query(Transfer)
            .filter(
                Transfer.asset_id == asset.asset_id,
                Transfer.status == TransferStatus.REQUESTED,
            )
            .first()
        )

        if existing_transfer:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A transfer request already exists for this asset.",
            )

        transfer = Transfer(
            asset_id=asset.asset_id,
            from_employee_id=from_employee.employee_id,
            to_employee_id=to_employee.employee_id,
            requested_by=requested_by,
            reason=reason,
        )

        db.add(transfer)

        try:
            db.commit()
            db.refresh(transfer)
            return transfer
        except Exception:
            db.rollback()
            raise

    @staticmethod
    def approve_transfer(
        db: Session,
        transfer: Transfer,
        asset,
        from_employee,
        to_employee,
        approved_by: int,
    ) -> Transfer:

        if transfer.status != TransferStatus.REQUESTED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only pending transfer requests can be approved.",
            )

        active_allocation = (
            db.query(Allocation)
            .filter(
                Allocation.asset_id == asset.asset_id,
                Allocation.employee_id == from_employee.employee_id,
                Allocation.status == AllocationStatus.ACTIVE,
            )
            .first()
        )

        if not active_allocation:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The original allocation is no longer active.",
            )

        # Close old allocation
        active_allocation.status = AllocationStatus.RETURNED
        active_allocation.returned_at = datetime.utcnow()

        # Create new allocation for destination employee
        new_allocation = Allocation(
            asset_id=asset.asset_id,
            employee_id=to_employee.employee_id,
            allocated_by=approved_by,
            status=AllocationStatus.ACTIVE,
        )

        db.add(new_allocation)

        transfer.status = TransferStatus.APPROVED
        transfer.approved_by = approved_by
        transfer.reviewed_at = datetime.utcnow()

        NotificationService.create_notification(
            db=db,
            user_id=to_employee.user_id,
            notification_type=NotificationType.TRANSFER,
            title="Asset Transfer Approved",
            message=f"Asset {asset.asset_tag} has been transferred to you.",
        )

        try:
            db.commit()
            db.refresh(transfer)
            return transfer
        except Exception:
            db.rollback()
            raise

    @staticmethod
    def reject_transfer(
        db: Session,
        transfer: Transfer,
        approved_by: int,
    ) -> Transfer:

        if transfer.status != TransferStatus.REQUESTED:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Only pending transfer requests can be rejected.",
            )

        transfer.status = TransferStatus.REJECTED
        transfer.approved_by = approved_by
        transfer.reviewed_at = datetime.utcnow()

        try:
            db.commit()
            db.refresh(transfer)
            return transfer
        except Exception:
            db.rollback()
            raise

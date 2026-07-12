from sqlalchemy.orm import Session

from app.models.allocation import Allocation, AllocationStatus
from app.schemas.allocation import AllocationCreate


class AllocationService:
    @staticmethod
    def create_allocation(db: Session, allocation_data: AllocationCreate):

        allocation = Allocation(
            asset_id=allocation_data.asset_id,
            employee_id=allocation_data.employee_id,
            allocated_by=allocation_data.allocated_by,
            expected_return_date=allocation_data.expected_return_date,
            status=AllocationStatus.ACTIVE,
        )

        db.add(allocation)
        db.commit()
        db.refresh(allocation)

        return allocation

    @staticmethod
    def get_allocations(db: Session):

        return db.query(Allocation).all()

from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.department import Department
from app.models.category import Category
from app.models.booking import Booking
from app.models.employee import Employee
from app.models.asset import Asset

class DashboardRepository:

    @staticmethod
    def total_assets(db: Session):
        return db.query(func.count(Asset.id)).scalar()

    @staticmethod
    def available_assets(db: Session):
        return db.query(func.count(Asset.id)).filter(
            Asset.status == "AVAILABLE"
        ).scalar()

    @staticmethod
    def allocated_assets(db: Session):
        return db.query(func.count(Asset.id)).filter(
            Asset.status == "ALLOCATED"
        ).scalar()

    @staticmethod
    def maintenance_assets(db: Session):
        return db.query(func.count(Asset.id)).filter(
            Asset.status == "MAINTENANCE"
        ).scalar()
    @staticmethod
    def department_allocation(db: Session):
        return (
            db.query(
    Department.name.label("name"),
    func.count(Asset.id).label("count")
)
            .join(
                Asset,
                Department.id == Asset.department_id
            )
            .group_by(Department.name)
            .all()
        )
    @staticmethod
    def category_distribution(db: Session):
        return (
            db.query(
    Category.name.label("name"),
    func.count(Asset.id).label("count")
)
            .join(
                Asset,
                Category.id == Asset.category_id
            )
            .group_by(Category.name)
            .all()
        )
    @staticmethod
    def recent_activity(db: Session):
        return (
            db.query(
                Employee.first_name,
                Employee.last_name,
                Asset.name,
                Booking.issue_date,
            )
            .join(
                Booking,
                Employee.id == Booking.employee_id,
            )
            .join(
                Asset,
                Asset.id == Booking.asset_id,
            )
            .order_by(
                Booking.issue_date.desc()
            )
            .limit(5)
            .all()
        )
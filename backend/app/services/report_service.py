from sqlalchemy.orm import Session

from app.repositories.report_repository import ReportRepository


class ReportService:

    @staticmethod
    def asset_status(db: Session):
        return ReportRepository.asset_status(db)
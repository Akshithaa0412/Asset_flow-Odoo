from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/asset-status")
def asset_status_report(db: Session = Depends(get_db)):
    return ReportService.asset_status(db)
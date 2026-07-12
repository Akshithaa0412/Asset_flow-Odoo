from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.asset import Asset


class ReportRepository:

    @staticmethod
    def asset_status(db: Session):
        result = (
            db.query(
                Asset.status,
                func.count(Asset.id).label("count")
            )
            .group_by(Asset.status)
            .all()
        )

        return [
            {
                "status": row.status,
                "count": row.count
            }
            for row in result
        ]
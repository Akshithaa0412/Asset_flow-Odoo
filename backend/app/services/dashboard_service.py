from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary(db: Session):

        total = DashboardRepository.total_assets(db)
        available = DashboardRepository.available_assets(db)
        allocated = DashboardRepository.allocated_assets(db)
        maintenance = DashboardRepository.maintenance_assets(db)

        department = DashboardRepository.department_allocation(db)
        category = DashboardRepository.category_distribution(db)
        activity = DashboardRepository.recent_activity(db)

        return {
            "kpis": {
                "total_assets": total,
                "available_assets": available,
                "allocated_assets": allocated,
                "maintenance_assets": maintenance,
            },

            "department_allocation": [
                {
                    "department": d.name,
                    "count": d.count
                }
                for d in department
            ],

            "category_distribution": [
                {
                    "category": c.name,
                    "count": c.count
                }
                for c in category
            ],

            "recent_activity": [
                {
                    "employee": f"{a.first_name} {a.last_name}",
                    "asset": a.name,
                    "issue_date": str(a.issue_date)
                }
                for a in activity
            ],

            "ai_insights": [
                f"{available} assets are idle and available for allocation.",
                f"{allocated} assets are currently allocated.",
                f"{maintenance} assets require maintenance attention.",
                (
                    "Asset utilization is healthy."
                    if available < allocated
                    else "Several assets appear underutilized."
                )
            ]
        }
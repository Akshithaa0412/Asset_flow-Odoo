from pydantic import BaseModel


class KPIResponse(BaseModel):
    total_assets: int
    available_assets: int
    allocated_assets: int
    maintenance_assets: int


class DepartmentAllocation(BaseModel):
    department: str
    count: int


class CategoryDistribution(BaseModel):
    category: str
    count: int


class Activity(BaseModel):
    employee: str
    asset: str
    issue_date: str


class DashboardResponse(BaseModel):
    kpis: KPIResponse
    department_allocation: list[DepartmentAllocation]
    category_distribution: list[CategoryDistribution]
    recent_activity: list[Activity]
    ai_insights: list[str]
from fastapi import FastAPI
from app.api.routes.reports import router as report_router
from app.db.database import Base, engine
from app.api.routes.assets import router as asset_router
from fastapi.middleware.cors import CORSMiddleware
# Import models so SQLAlchemy knows about them
from app.models import (
    Department,
    Category,
    Vendor,
    Employee,
    Asset,
    Booking,
    Maintenance
)
from app.api.routes.dashboard import router as dashboard_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AssetFlow API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(asset_router)
app.include_router(dashboard_router)
app.include_router(report_router)
@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AssetFlow Backend Ready 🚀"
    }

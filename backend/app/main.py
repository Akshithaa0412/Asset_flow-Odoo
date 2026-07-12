from fastapi import FastAPI

from app.db.database import Base, engine
from app.api.routes.assets import router as asset_router
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
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AssetFlow API",
    version="1.0.0"
)
app.include_router(asset_router)

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AssetFlow Backend Ready 🚀"
    }

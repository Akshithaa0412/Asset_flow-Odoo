from fastapi import FastAPI

from app.database import engine, Base
from app.api import allocations

from app.models.allocation import Allocation


Base.metadata.create_all(bind=engine)


app = FastAPI(title="AssetFlow API", version="1.0.0")


app.include_router(allocations.router)


@app.get("/")
def root():
    return {"success": True, "message": "AssetFlow API is running", "data": {}}

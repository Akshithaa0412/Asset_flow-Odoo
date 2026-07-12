from fastapi import FastAPI
from app.api import allocations

app = FastAPI(title="AssetFlow API", version="1.0.0")

app.include_router(allocations.router)


@app.get("/")
def root():
    return {"success": True, "message": "AssetFlow API is running", "data": {}}

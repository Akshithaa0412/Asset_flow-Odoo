import app.models
from fastapi import FastAPI
from sqlalchemy import text
from app.api.department import router as department_router
from app.database.session import engine
from app.api.auth import router as auth_router

app = FastAPI(title="AssetFlow API")
app.include_router(auth_router)
app.include_router(department_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to AssetFlow API 🚀"
    }


@app.get("/test-db")
def test_database():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT NOW();"))

        current_time = result.scalar()

    return {
        "status": "Connected ✅",
        "server_time": current_time
    }
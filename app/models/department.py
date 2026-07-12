from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True)

    department_name = Column(String(100), unique=True, nullable=False)

    status = Column(String(20), default="Active")

    created_at = Column(DateTime, server_default=func.now())
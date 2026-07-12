from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    employee_name = Column(String(100), nullable=False)

    phone = Column(String(20))

    department_id = Column(Integer, ForeignKey("departments.department_id"))

    designation = Column(String(100))

    status = Column(String(20), default="Active")

    created_at = Column(DateTime, server_default=func.now())
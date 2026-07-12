from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.employee import (
    EmployeeUpdate,
    EmployeeResponse,
    StatusUpdate,
)

from app.services.employee_services import (
    get_all_employees,
    get_employee,
    update_employee,
    update_employee_status,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_one(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update(
    employee_id: int,
    request: EmployeeUpdate,
    db: Session = Depends(get_db),
):
    employee = update_employee(db, employee_id, request)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.patch("/{employee_id}/status")
def update_status(
    employee_id: int,
    request: StatusUpdate,
    db: Session = Depends(get_db),
):
    employee = update_employee_status(
        db,
        employee_id,
        request.status,
    )

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee status updated successfully"}
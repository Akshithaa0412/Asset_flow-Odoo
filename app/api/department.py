from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from app.services.department_service import (
    create_department,
    get_departments,
    get_department,
    update_department,
    deactivate_department,
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post("/", response_model=DepartmentResponse)
def create(department: DepartmentCreate, db: Session = Depends(get_db)):
    result = create_department(
        db,
        department.department_name,
        department.parent_department_id
    )

    if result is None:
        raise HTTPException(
            status_code=400,
            detail="Department already exists"
        )

    return result


@router.get("/", response_model=list[DepartmentResponse])
def get_all(db: Session = Depends(get_db)):
    return get_departments(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_one(department_id: int, db: Session = Depends(get_db)):
    department = get_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update(
    department_id: int,
    request: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    department = update_department(
        db,
        department_id,
        request.department_name
    )

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.delete("/{department_id}")
def delete(department_id: int, db: Session = Depends(get_db)):
    department = deactivate_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deactivated successfully"
    }
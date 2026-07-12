from sqlalchemy.orm import Session
from app.models.department import Department


def create_department(db: Session, department_name: str, parent_department_id=None):

    existing = db.query(Department).filter(
        Department.department_name == department_name
    ).first()

    if existing:
        return None

    department = Department(
        department_name=department_name,
        parent_department_id=parent_department_id,
        status="Active"
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department


def get_departments(db: Session):
    return db.query(Department).all()


def get_department(db: Session, department_id: int):
    return db.query(Department).filter(
        Department.department_id == department_id
    ).first()


def update_department(db: Session, department_id: int, department_name: str):

    department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if not department:
        return None

    department.department_name = department_name

    db.commit()
    db.refresh(department)

    return department


def deactivate_department(db: Session, department_id: int):

    department = db.query(Department).filter(
        Department.department_id == department_id
    ).first()

    if not department:
        return None

    department.status = "Inactive"

    db.commit()

    return department
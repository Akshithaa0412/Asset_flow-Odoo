from sqlalchemy.orm import Session

from app.models.employee import Employee


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()


def update_employee(db: Session, employee_id: int, data):

    employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if employee is None:
        return None

    employee.employee_name = data.employee_name
    employee.phone = data.phone
    employee.department_id = data.department_id
    employee.designation = data.designation

    db.commit()
    db.refresh(employee)

    return employee


def update_employee_status(db: Session, employee_id: int, status: str):

    employee = db.query(Employee).filter(
        Employee.employee_id == employee_id
    ).first()

    if employee is None:
        return None

    employee.status = status

    db.commit()
    db.refresh(employee)

    return employee
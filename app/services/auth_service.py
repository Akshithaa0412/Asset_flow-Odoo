from sqlalchemy.orm import Session

from app.models.user import User
from app.models.employee import Employee
from app.core.security import hash_password


def signup_user(db: Session, email: str, password: str, employee_name: str):

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        return None

    new_user = User(
        email=email,
        password=hash_password(password),
        role="EMPLOYEE",
        status="Active"
    )

    db.add(new_user)
    db.flush()   # Generates user_id

    employee = Employee(
        user_id=new_user.user_id,
        employee_name=employee_name,
        status="Active"
    )

    db.add(employee)

    db.commit()

    db.refresh(new_user)

    return new_user
from app.core.security import verify_password
from app.core.auth import create_access_token


def login_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token({
        "user_id": user.user_id,
        "email": user.email,
        "role": user.role
    })

    return token
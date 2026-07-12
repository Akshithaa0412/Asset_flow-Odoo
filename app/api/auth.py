from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import SignupRequest
from app.database.session import get_db
from app.services.auth_service import signup_user
from app.schemas.auth import LoginRequest
from app.services.auth_service import login_user
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db)
):

    user = signup_user(
        db,
        request.email,
        request.password,
        request.employee_name
    )

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )

    return {
        "message": "User created successfully",
        "user_id": user.user_id
    }
@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        request.email,
        request.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=30)

    payload.update({"exp": expire})

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
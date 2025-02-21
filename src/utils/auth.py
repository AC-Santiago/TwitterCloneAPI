from datetime import datetime, timedelta, timezone
import os
from typing import Annotated, Optional
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends
from dotenv import load_dotenv

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def encode_token(
    payload: dict, expires_delta: Optional[timedelta] = None
) -> str:
    to_encode: dict = payload.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

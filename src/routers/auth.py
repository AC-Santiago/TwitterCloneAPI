from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Header, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from crud.user import create_user, get_user_by_email
from database.connection import get_session
from models.models import Users
from schemas.user import UserCreate
from utils.auth import encode_token
from utils.security import (
    add_token_to_blacklist,
    is_token_blacklisted,
    verify_password,
)

router = APIRouter()


@router.post("/login", tags=["auth"], response_model=Users)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)],
):

    user = get_user_by_email(db=session, email=form_data.username)
    if not user or not verify_password(
        plain_password=form_data.password, hashed_password=user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = encode_token(
        {"email": form_data.username, "full_name": user.full_name}
    )
    return JSONResponse(
        content={"access_token": access_token}, status_code=status.HTTP_200_OK
    )


@router.post("/register", tags=["auth"], response_model=Users)
def register(
    user: UserCreate, session: Annotated[Session, Depends(get_session)]
):
    db_user = get_user_by_email(db=session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        create_user(db=session, user=user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
    return JSONResponse(
        content={"message": "Usuario creado exitosamente"},
        status_code=status.HTTP_201_CREATED,
    )


@router.post("/logout")
def logout(
    authorization: Annotated[str, Header(..., alias="Authorization")],
    db: Annotated[Session, Depends(get_session)],
):
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format",
        )
    token = authorization.split(" ")[1]
    if is_token_blacklisted(db, token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has already"
        )
    add_token_to_blacklist(db, token)
    return {"message": "Successfully logged out"}

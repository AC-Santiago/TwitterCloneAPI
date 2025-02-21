from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from sqlmodel import select

from database.connection import get_session
from models.user import Users

router = APIRouter()


@router.get("/users/{user_id}", response_model=Users)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=List[Users])
def read_users(session: Session = Depends(get_session)):
    users = session.exec(select(Users)).all()
    return users


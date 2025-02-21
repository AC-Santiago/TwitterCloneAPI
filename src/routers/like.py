from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from sqlmodel import select

from database.connection import get_session
from models.like import Likes

router = APIRouter()


@router.get("/likes/{like_id}", response_model=Likes)
def read_like(like_id: int, session: Session = Depends(get_session)):
    like = session.get(Likes, like_id)
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    return like

@router.get("/likes/", response_model=List[Likes])
def read_likes(session: Session = Depends(get_session)):
    likes = session.exec(select(Likes)).all()
    return likes
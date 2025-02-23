from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from sqlmodel import select

from database.connection import get_session
from models.models import Comment

router = APIRouter()


@router.get("/{comment_id}", response_model=Comment)
def read_comment(comment_id: int, session: Session = Depends(get_session)):
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.get("/", response_model=List[Comment])
def read_comments(session: Session = Depends(get_session)):
    comments = session.exec(select(Comment)).all()
    return comments

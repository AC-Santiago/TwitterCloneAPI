from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import Annotated, List


from crud.user import get_user_by_email
from database.connection import get_session
from schemas.like import LikeCreate, LikeOut, LikeCreateRequest
from crud.like import (
    create_like,
    get_like,
    get_likes,
    get_likes_by_tweet,
    get_likes_by_user,
    delete_like,
)
from utils.auth import decode_token

router = APIRouter()


@router.post("/likes/", response_model=LikeOut)
def create_likes(
    session: Annotated[Session, Depends(get_session)],
    like: LikeCreateRequest,
    user: Annotated[dict, Depends(decode_token)],
):
    user_id: int = get_user_by_email(session, user["email"]).id
    like_create = LikeCreate(tweet_id=like.tweet_id, user_id=user_id)
    new_like = create_like(session, like_create)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "id_like": new_like.id,
            "tweet_id": new_like.tweet_id,
            "user_name": get_user_by_email(session, user["email"]).name,
        },
    )


@router.get("/likes/{like_id}", response_model=LikeOut)
def read_like(like_id: int, session: Annotated[Session, Depends(get_session)]):
    like = get_like(session, like_id)
    if not like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Like no encontrado"
        )
    return like


@router.get("/likes/", response_model=List[LikeOut])
def read_likes(session: Annotated[Session, Depends(get_session)]):
    return get_likes(session)


@router.get("/likes/tweet/{tweet_id}", response_model=List[LikeOut])
def read_likes_by_tweet(
    tweet_id: int, session: Annotated[Session, Depends(get_session)]
):
    return get_likes_by_tweet(session, tweet_id)


@router.get("/likes/user/{user_id}", response_model=List[LikeOut])
def read_likes_by_user(
    user_id: int, session: Annotated[Session, Depends(get_session)]
):
    user_likes = get_likes_by_user(session, user_id)
    if not user_likes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron likes para este usuario",
        )
    return user_likes


@router.delete("/likes/{like_id}", response_model=LikeOut)
def delete_likes(
    like_id: int,
    session: Annotated[Session, Depends(get_session)],
    user: Annotated[dict, Depends(decode_token)],
):
    like = get_like(session, like_id)
    if not like:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Like no encontrado"
        )

    user_id = get_user_by_email(session, user["email"]).id
    if like.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No puedes eliminar likes de otros usuarios",
        )
    delete_like(session, like_id)
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"detail": "Like eliminado correctamente"},
    )

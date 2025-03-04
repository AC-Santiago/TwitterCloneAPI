from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List


from crud.comment import (
    get_comment,
    get_comments_by_tweet,
    create_comment,
    delete_comment,
    update_comment,
)
from database.connection import get_session

from schemas.comment import CommentCreate, CommentOut
from utils.auth import decode_token, oauth2_scheme

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("/tweet/comment", response_model=CommentOut)
async def create_comment_router(
    comment: CommentCreate,
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
):

    token_data = decode_token(token)
    user_id = token_data.get("sub")

    return create_comment(
        db=session,
        tweet_id=comment.tweet_id,
        user_id=user_id,
        contenido=comment.contenido,
    )


@router.get("/tweet/comment/{comment_id}", response_model=CommentOut)
async def read_comment_router(
    comment_id: int, session: Session = Depends(get_session)
):
    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comment


@router.get("/tweet/{tweet_id}", response_model=List[CommentOut])
async def get_comments_by_tweet_router(
    tweet_id: int, session: Session = Depends(get_session)
):
    return get_comments_by_tweet(db=session, tweet_id=tweet_id)


@router.delete("/{comment_id}")
async def delete_comment_router(
    comment_id: int,
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
):

    token_data = decode_token(token)
    user_id = token_data.get("sub")

    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    if comment.usuario_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="No tienes permiso para eliminar este comentario",
        )

    delete_comment(db=session, comment=comment)
    return {"message": "Comentario eliminado exitosamente"}


@router.put("/{comment_id}", response_model=CommentOut)
async def update_comment_router(
    comment_id: int,
    comment_update: CommentCreate,
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
):

    token_data = decode_token(token)
    user_id = token_data.get("sub")

    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    if comment.usuario_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="No tienes permiso para actualizar este comentario",
        )

    return update_comment(
        db=session, comment=comment, contenido=comment_update.contenido
    )

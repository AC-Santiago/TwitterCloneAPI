from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import Annotated, List


from crud.comment import (
    get_comment,
    get_comments_by_tweet,
    create_comment,
    delete_comment,
    update_comment,
)
from crud.user import get_user_by_email
from database.connection import get_session

from models.models import Comments
from schemas.comment import CommentCreate, CommentOut, CommentEdit
from utils.auth import decode_token

router = APIRouter(tags=["comments"])


@router.post("/tweet/comment", response_model=CommentOut)
async def create_comment_router(
    comment: CommentCreate,
    user: Annotated[dict, Depends(decode_token)],
    session: Session = Depends(get_session),
):

    user_id: int = get_user_by_email(session, user["email"]).id

    new_comment: Comments = create_comment(
        db=session,
        tweet_id=comment.tweet_id,
        user_id=user_id,
        contenido=comment.contenido,
    )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "id": new_comment.id,
            "tweet_id": new_comment.tweet_id,
            "usuario_id": new_comment.usuario_id,
            "contenido": new_comment.contenido,
        },
    )


@router.get("/tweet/comment/{comment_id}", response_model=CommentOut)
async def read_comment_router(
    comment_id: int, session: Session = Depends(get_session)
):
    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comentario no existe",
        )
    return comment


@router.get("/tweet/{tweet_id}", response_model=List[CommentOut])
async def get_comments_by_tweet_router(
    tweet_id: int, session: Session = Depends(get_session)
):
    comments = get_comments_by_tweet(db=session, tweet_id=tweet_id)
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se encontraron comentarios para este tweet",
        )
    return comments


@router.delete("/{comment_id}")
async def delete_comment_router(
    comment_id: int,
    user: Annotated[dict, Depends(decode_token)],
    session: Session = Depends(get_session),
):

    user_id: int = get_user_by_email(session, user["email"]).id

    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comentario no existe",
        )

    if comment.usuario_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permiso para eliminar este comentario",
        )

    delete_comment(db=session, comment=comment)
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"detail": "Comentario eliminado"},
    )


@router.put("/{comment_id}", response_model=CommentOut)
async def update_comment_router(
    comment_id: int,
    comment_update: CommentEdit,
    user: Annotated[dict, Depends(decode_token)],
    session: Annotated[Session, Depends(get_session)],
):

    user_id = get_user_by_email(session, user["email"]).id

    comment = get_comment(db=session, comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    if comment.usuario_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="No tienes permiso para actualizar este comentario",
        )

    updated_comment = update_comment(
        db=session, comment=comment, contenido=comment_update.contenido
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "id": updated_comment.id,
            "tweet_id": updated_comment.tweet_id,
            "usuario_id": updated_comment.usuario_id,
            "contenido": updated_comment.contenido,
        },
    )

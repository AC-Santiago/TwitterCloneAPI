from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import Annotated, List
from sqlmodel import select

from crud.tweet import (
    get_tweets_with_likes_by_user,
    get_tweets_with_retweets_by_user,
)
from crud.user import get_user_by_email
from database.connection import get_session
from models.models import Tweets, Users
from utils.auth import decode_token

router = APIRouter()


@router.get("/profile/", response_model=Users)
def read_user(
    user: Annotated[dict, Depends(decode_token)],
    session: Session = Depends(get_session),
):
    user_id = get_user_by_email(session, user["email"]).id
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/", response_model=List[Users])
def read_users(session: Session = Depends(get_session)):
    users = session.exec(select(Users)).all()
    return users


@router.get("/users/tweets/liked", response_model=List[Tweets])
def get_tweets_liked_by_user(
    user: Annotated[dict, Depends(decode_token)],
    session: Session = Depends(get_session),
):
    user_id = get_user_by_email(session, user["email"]).id
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tweets = get_tweets_with_likes_by_user(user_id, session)

    return tweets


@router.get("/users/tweets/retweeted", response_model=List[Tweets])
def get_tweets_retweeted_by_user(
    user: Annotated[dict, Depends(decode_token)],
    session: Session = Depends(get_session),
):
    user_id = get_user_by_email(session, user["email"]).id
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tweets = get_tweets_with_retweets_by_user(user_id, session)
    return tweets

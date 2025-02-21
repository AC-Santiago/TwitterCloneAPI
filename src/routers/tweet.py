from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import Annotated, List
from sqlmodel import select

from crud.tweet import create_tweet, get_tweet, get_tweets
from crud.user import get_user_by_email
from database.connection import get_session
from models.models import Tweets
from schemas.tweet import TweetBase, TweetCreate
from utils.auth import decode_token

router = APIRouter()


@router.get("/tweets/{tweet_id}", response_model=Tweets)
def read_tweet(tweet_id: int, session: Session = Depends(get_session)):
    tweet = get_tweet(session, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return tweet


@router.get("/tweets/", response_model=List[Tweets])
def read_tweets(session: Session = Depends(get_session)):
    tweets = get_tweets(session)
    return tweets


@router.post("/tweet/")
def create_tweets(
    session: Annotated[Session, Depends(get_session)],
    new_tweet: TweetBase,
    user: Annotated[dict, Depends(decode_token)],
):
    user_id = get_user_by_email(session, user["email"]).id
    tweet = TweetCreate(user_id=user_id, content=new_tweet.content)
    create_tweet(session, tweet)
    return JSONResponse(
        {"message": "Tweet successfully created"},
        status_code=status.HTTP_201_CREATED,
    )

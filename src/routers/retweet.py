from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from sqlmodel import select

from database.connection import get_session
from models.retweet import Retweet

router = APIRouter()


@router.get("/tweets/{tweet_id}", response_model=Retweet)
def read_tweet(tweet_id: int, session: Session = Depends(get_session)):
    tweet = session.get(Retweet, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return tweet

@router.get("/tweets/", response_model=List[Retweet])
def read_tweets(session: Session = Depends(get_session)):
    tweets = session.exec(select(Retweet)).all()
    return tweets
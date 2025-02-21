from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import Session
from typing import Annotated, List

from crud.tweet import count_likes, create_tweet, get_tweet, get_tweets, count_retweets
from crud.user import get_user_by_email
from database.connection import get_session
from models.models import Tweets
from schemas.tweet import TweetBase, TweetCreate
from utils.auth import decode_token

router = APIRouter()


@router.get("/tweets/{tweet_id}", tags=["Tweets"], response_model=Tweets)
def read_tweet(tweet_id: int, session: Session = Depends(get_session)):
    tweet = get_tweet(session, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")
    return tweet


@router.get("/tweets/", tags=["Tweets"], response_model=List[Tweets])
def read_tweets(session: Session = Depends(get_session)):
    tweets = get_tweets(session)
    return tweets


@router.post("/tweet/", tags=["Tweets"])
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


@router.get("/tweets/{tweet_id}/likes/count", tags=["Tweets"])
def get_likes_count(tweet_id: int, session: Session = Depends(get_session)):
    tweet = session.get(Tweets, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")

    total_likes = count_likes(tweet_id, session)

    return {"tweet_id": tweet_id, "total_likes": total_likes}


@router.get("/tweets/{tweet_id}/retweets/count", tags=["Tweets"])
def get_retweets_count(tweet_id: int, session: Session = Depends(get_session)):
    tweet = session.get(Tweets, tweet_id)
    if not tweet:
        raise HTTPException(status_code=404, detail="Tweet not found")

    total_retweets = count_retweets(tweet_id, session)

    return {"tweet_id": tweet_id, "total_retweets": total_retweets}



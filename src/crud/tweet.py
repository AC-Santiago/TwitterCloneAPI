from sqlmodel import Session, select

from models.models import Tweets
from schemas.tweet import TweetCreate


def get_tweet(db: Session, tweet_id: int):
    return db.exec(select(Tweets).where(Tweets.id == tweet_id)).first()


def get_tweets_by_user(db: Session, user_id: int):
    return db.exec(select(Tweets).where(Tweets.user_id == user_id)).all()


def get_tweets(db: Session):
    return db.exec(select(Tweets)).all()


def create_tweet(db: Session, tweet: TweetCreate):
    db_tweet = Tweets(user_id=tweet.user_id, contenido=tweet.content)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet

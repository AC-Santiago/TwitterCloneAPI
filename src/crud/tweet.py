from sqlmodel import Session, select, func

from models.models import Likes, Tweets, Retweets, Users
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


def count_likes(tweet_id: int, session: Session):
    total_likes = session.exec(
        select(func.count()).where(Likes.tweet_id == tweet_id)
    ).one()
    return total_likes


def get_tweets_with_likes_by_user(user_id: int, session: Session):
    tweets = session.exec(
        select(Tweets).join(Likes).where(Likes.user_id == user_id)
    ).all()

    return tweets


def get_tweets_with_retweets_by_user(user_id: int, session: Session):
    tweets = session.exec(
        select(Tweets).join(Retweets).where(Retweets.user_id == user_id)
    ).all()

    return tweets


def count_retweets(tweet_id: int, session: Session):
    total_retweets = session.exec(
        select(func.count()).where(Retweets.tweet_id == tweet_id)
    ).one()

    return total_retweets


def get_tweets_with_username(db: Session):
    results = db.exec(
        select(Tweets, Users.name).join(Users, Users.id == Tweets.user_id)
    ).all()
    tweets = []
    for tweet, username in results:
        tweets.append(
            {
                "id": tweet.id,
                "contenido": tweet.contenido,
                "user_name": username,
            }
        )
    return tweets

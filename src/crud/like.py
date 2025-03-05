from sqlmodel import Session, select
from models.models import Likes
from schemas.like import LikeCreate

def create_like(db: Session, like: LikeCreate) -> Likes:
    db_like = Likes(tweet_id=like.tweet_id, user_id=like.user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def get_like(db: Session, like_id: int) -> Likes:
    return db.get(Likes, like_id)

def get_likes(db: Session):
    return db.exec(select(Likes)).all()

def get_likes_by_tweet(db: Session, tweet_id: int):
    return db.exec(select(Likes).where(Likes.tweet_id == tweet_id)).all()

def get_likes_by_user(db: Session, user_id: int):
    return db.exec(select(Likes).where(Likes.user_id == user_id)).all()

def delete_like(db: Session, like_id: int):
    like = db.get(Likes, like_id)
    if like:
        db.delete(like)
        db.commit()
    return like


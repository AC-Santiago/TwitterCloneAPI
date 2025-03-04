from sqlmodel import Session, select
from models.models import Comments


def create_comment(db: Session, tweet_id: int, user_id: int, contenido: str):
    db_comment = Comments(
        tweet_id=tweet_id, usuario_id=user_id, contenido=contenido
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.get(Comments, comment_id)


def get_comments_by_tweet(db: Session, tweet_id: int):
    return db.exec(select(Comments).where(Comments.tweet_id == tweet_id)).all()


def delete_comment(db: Session, comment: Comments):
    db.delete(comment)
    db.commit()


def update_comment(db: Session, comment: Comments, contenido: str):
    comment.contenido = contenido
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

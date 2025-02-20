from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate
from utils.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.exec(select(User).where(User.id == user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).where(User.email == email)).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

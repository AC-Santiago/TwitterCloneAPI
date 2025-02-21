from sqlmodel import Session, select
from models.user import Users
from schemas.user import UserCreate
from utils.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.exec(select(User).where(User.id == user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).where(User.email == email)).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        full_name=user.full_name,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def change_picture(db: Session, user_id: int, file_path: str):
    user = db.exec(select(User).where(User.id == user_id)).first()
    user.picture = file_path
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

from typing import Optional
from sqlmodel import Session, select
from models.models import Users
from schemas.user import UserCreate
from utils.security import get_password_hash


def get_user(db: Session, user_id: int):
    return db.exec(select(Users).where(Users.id == user_id)).first()


def get_user_by_email(db: Session, email: str):
    return db.exec(select(Users).where(Users.email == email)).first()


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = Users(
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
    user = db.exec(select(Users).where(Users.id == user_id)).first()
    user.picture = file_path
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_info(db: Session, user_id: int, new_name: Optional[str] = None, new_password: Optional[str] = None):
    user = db.exec(select(Users).where(Users.id == user_id)).first()
    if not user:
        return None
    if new_name:
        user.name = new_name
    if new_password:
        user.password = get_password_hash(new_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

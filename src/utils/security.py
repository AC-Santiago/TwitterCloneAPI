import bcrypt
from sqlmodel import Session, select

from models.token_blacklist import TokenBlacklist


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def add_token_to_blacklist(db: Session, token: str):
    db_token = TokenBlacklist(token=token)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)


def is_token_blacklisted(db: Session, token: str) -> bool:
    return (
        db.exec(
            select(TokenBlacklist).where(TokenBlacklist.token == token)
        ).first()
        is not None
    )

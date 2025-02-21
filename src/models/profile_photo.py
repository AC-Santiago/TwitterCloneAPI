from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from models.user import User


class ProfilePhoto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    file_name: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    user_id: int = Field(foreign_key="user.id", unique=True)

    user: Optional["User"] = Relationship(back_populates="profile_photo")

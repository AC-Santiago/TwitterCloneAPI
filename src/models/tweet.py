from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

from models.comment import Comment
from models.like import Like
from models.user import User


class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(default=None)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional["User"] = Relationship(back_populates="tweets")
    comments: List["Comment"] = Relationship(back_populates="tweet")
    likes: List["Like"] = Relationship(back_populates="tweet")

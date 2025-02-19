from typing import List, Optional
from tweet import Tweet
from comment import Comment
from like import Like
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(index=True)

    tweets: List["Tweet"] = Relationship(back_populates="user")
    comments: List["Comment"] = Relationship(back_populates="user")
    likes: List["Like"] = Relationship(back_populates="user")

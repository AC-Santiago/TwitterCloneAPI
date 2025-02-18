from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    tweet_id: Optional[int] = Field(default=None, foreign_key="tweet.id")

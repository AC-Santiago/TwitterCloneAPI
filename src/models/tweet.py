from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(default=None)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

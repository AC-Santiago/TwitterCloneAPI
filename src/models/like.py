from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Likes(SQLModel, table=True):
    like_id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweet.tweet_id")
    usuario_id: int 

    # Relación con Tweet
    tweet: Optional[Tweet] = Relationship(back_populates="likes")

  
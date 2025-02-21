from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

class Retweet(SQLModel, table=True):
    retweet_id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweet.tweet_id")
    usuario_id: int = Field(foreign_key="users.id")
    contenido: str
 
    # Relación con Tweet
    tweet: Optional[Tweet] = Relationship(back_populates="retweets")


from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from sqlmodel import SQLModel, Field


class Retweet(SQLModel, table=True):
    retweet_id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweet.tweet_id")
    usuario_id: int 
    contenido: str
 


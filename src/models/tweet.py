from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from sqlmodel import SQLModel, Field
from models.comment import Comment
from models.like import Likes
from models.retweet import Retweet

class Tweet(SQLModel, table=True):
    tweet_id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="users.id")
    contenido: str
  

    # Relación con Comentario
    comments: List["Comment"] = Relationship(back_populates="tweet")

    # Relación con Likes
    likes: List["Likes"] = Relationship(back_populates="tweet")

    # Relación con Retweet
    retweets: List["Retweet"] = Relationship(back_populates="tweet")

    
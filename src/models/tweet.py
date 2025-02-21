from typing import Optional
from sqlmodel import SQLModel, Field


class Tweet(SQLModel, table=True):
    tweet_id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="users.id")
    contenido: str

    # Relación con Users
    usuario: Optional[Users] = Relationship(back_populates="tweets")

    # Relación con Comentario
    comentarios: list["Comentario"] = Relationship(back_populates="tweet")

    # Relación con Likes
    likes: list["Likes"] = Relationship(back_populates="tweet")

    # Relación con Retweet
    retweets: list["Retweet"] = Relationship(back_populates="tweet")

    
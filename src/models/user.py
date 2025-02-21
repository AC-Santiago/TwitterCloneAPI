from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=10)
    email: str = Field(max_length=10)
    password: str = Field(max_length=10)


    # Relación con Tweet
    tweets: list["Tweet"] = Relationship(back_populates="usuario")

    # Relación con Comentario
    comentarios: list["Comentario"] = Relationship(back_populates="usuario")

    # Relación con Likes
    likes: list["Likes"] = Relationship(back_populates="usuario")

    # Relación con Retweet
    retweets: list["Retweet"] = Relationship(back_populates="usuario")
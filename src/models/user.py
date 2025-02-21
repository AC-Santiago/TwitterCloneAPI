from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from models.tweet import Tweet
from models.comment import Comment
from models.like import Likes
from models.retweet import Retweet
from models.profile_photo import ProfilePhoto


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(default=None)
    full_name: str = Field(default=None)
    biography: str = Field(default="")

    # Relación con Tweet
    tweets: List["Tweet"] = Relationship(back_populates="usuario")

    # Relación con Comentario
    comentarios: List["Comment"] = Relationship(back_populates="usuario")

    # Relación con Likes
    likes: List["Likes"] = Relationship(back_populates="usuario")

    # Relación con Retweet
    retweets: List["Retweet"] = Relationship(back_populates="usuario")

    profile_photo: Optional["ProfilePhoto"] = Relationship(
        back_populates="user"
    )

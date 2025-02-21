from datetime import datetime, timezone
from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(default=None)
    full_name: str = Field(default=None)
    biography: str = Field(default="")

    # Relación con Tweet
    tweets: List["Tweets"] = Relationship(back_populates="user")

    profile_photo: Optional["ProfilePhotos"] = Relationship(
        back_populates="user"
    )


# Modelo Tweet
class Tweets(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    contenido: str

    # Relación con Users
    user: Optional[Users] = Relationship(back_populates="tweets")

    # Relación con Comentario
    comments: List["Comments"] = Relationship(back_populates="tweet")

    # Relación con Likes
    likes: List["Likes"] = Relationship(back_populates="tweet")

    # Relación con Retweet
    retweets: List["Retweets"] = Relationship(back_populates="tweet")


# Modelo Comentario
class Comments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweets.id")
    usuario_id: int
    contenido: str

    # Relación con Tweet
    tweet: Optional[Tweets] = Relationship(back_populates="comments")


# Modelo Likes
class Likes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweets.id")
    user_id: int
    # Relación con Tweet
    tweet: Optional[Tweets] = Relationship(back_populates="likes")


# Modelo Retweet
class Retweets(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tweet_id: int = Field(foreign_key="tweets.id")
    usuario_id: int
   
    # Relación con Tweet
    tweet: Optional[Tweets] = Relationship(back_populates="retweets")


# Modelo de las foto de perfil
class ProfilePhotos(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    file_path: str
    file_name: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    user_id: int = Field(foreign_key="users.id", unique=True)

    user: Optional[Users] = Relationship(back_populates="profile_photo")

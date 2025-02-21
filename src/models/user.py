from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str = Field(default=None)
    full_name: str = Field(default=None)
    biography: str = Field(default="")
    picture: str = Field(default="")

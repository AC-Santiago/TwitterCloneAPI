from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    full_name: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None
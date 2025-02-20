from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = constr(min_length=6)

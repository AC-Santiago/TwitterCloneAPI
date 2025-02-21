from pydantic import BaseModel, Field


class TweetCreate(BaseModel):
    user_id: int
    content: str = Field(max_length=280)


class TweetBase(BaseModel):
    content: str = Field(max_length=280)

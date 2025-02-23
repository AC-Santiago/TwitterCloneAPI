from pydantic import BaseModel, Field


class TweetCreate(BaseModel):
    user_id: int
    content: str = Field(max_length=280)


class TweetBase(BaseModel):
    content: str = Field(max_length=280)


class TweetOut(TweetBase):
    content: str = Field(max_length=280)
    user_name: str

    class Config:
        orm_mode = True

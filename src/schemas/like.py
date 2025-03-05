from pydantic import BaseModel


class LikeCreate(BaseModel):
    tweet_id: int
    user_id: int


class LikeOut(BaseModel):
    id: int
    tweet_id: int
    user_id: int

from pydantic import BaseModel


class CommentCreate(BaseModel):
    tweet_id: int
    contenido: str


class CommentOut(BaseModel):
    id: int
    tweet_id: int
    usuario_id: int
    contenido: str

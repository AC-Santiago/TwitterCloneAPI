from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class TokenBlacklist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    token: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))

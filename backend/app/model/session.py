from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column
from datetime import datetime, timezone


class Session(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    user_id: UUID = Field(foreign_key="user.id")
    topic: str
    session_type: str
    status: str
    messages: dict = Field(default_factory=dict, sa_column=Column(JSONB))
    elapsed_time: float = Field(default=0)
    paused_at: datetime | None = None
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    ended_at: datetime | None = None
    deleted_at: datetime | None = None
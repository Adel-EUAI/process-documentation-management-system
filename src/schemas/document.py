from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    title: str
    description: str | None = None


class DocumentUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

from datetime import datetime


class DocumentOut(BaseModel):
    id: int
    title: str
    description: str | None
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)






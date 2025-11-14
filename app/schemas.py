from typing import Optional
from sqlmodel import SQLModel


class TermCreate(SQLModel):
    keyword: str
    description: str


class TermRead(SQLModel):
    id: int
    keyword: str
    description: str


class TermUpdate(SQLModel):
    description: Optional[str] = None

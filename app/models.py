from typing import Optional
from sqlmodel import SQLModel, Field


class Term(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    keyword: str = Field(index=True, nullable=False, max_length=100)
    description: str

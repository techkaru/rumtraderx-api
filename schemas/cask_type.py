from datetime import datetime
from pydantic import BaseModel


class CaskTypeBase(BaseModel):
    name: str
    description: str


class CaskTypeCreate(CaskTypeBase):
    pass


class CaskType(CaskTypeBase):
    id: int

    class Config:
        from_attributes = True

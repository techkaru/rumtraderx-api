from datetime import datetime
from pydantic import BaseModel


class DistilleryBase(BaseModel):
    name: str
    description: str
    creation_date: datetime
    is_alive: bool
    closure_date: datetime | None = None
    country: str
    region: str | None = None


class DistilleryCreate(DistilleryBase):
    pass


class Distillery(DistilleryBase):
    id: int

    class Config:
        from_attributes = True

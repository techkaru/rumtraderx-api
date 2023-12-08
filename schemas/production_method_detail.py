from datetime import datetime
from pydantic import BaseModel


class ProductionMethodDetailBase(BaseModel):
    name: str
    description: str | None = None


class ProductionMethodDetailCreate(ProductionMethodDetailBase):
    pass


class ProductionMethodDetail(ProductionMethodDetailBase):
    id: int

    class Config:
        from_attributes = True

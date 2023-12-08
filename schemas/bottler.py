from pydantic import BaseModel


class BottlerBase(BaseModel):
    name: str
    description: str
    country: str
    region: str | None = None


class BottlerCreate(BottlerBase):
    pass


class Bottler(BottlerBase):
    id: int

    class Config:
        from_attributes = True

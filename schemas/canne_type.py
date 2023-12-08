from pydantic import BaseModel


class CanneTypeBase(BaseModel):
    name: str
    description: str


class CanneTypeCreate(CanneTypeBase):
    pass


class CanneType(CanneTypeBase):
    id: int

    class Config:
        from_attributes = True

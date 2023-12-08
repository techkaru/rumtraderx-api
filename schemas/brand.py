from pydantic import BaseModel


class BrandBase(BaseModel):
    name: str
    description: str
    country: str
    region: str | None = None


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int

    class Config:
        from_attributes = True

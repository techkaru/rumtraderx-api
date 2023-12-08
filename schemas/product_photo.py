from datetime import datetime
from pydantic import BaseModel


class ProductPhotoBase(BaseModel):
    external_id: str
    url: str
    product_id: str


class ProductPhotoCreate(ProductPhotoBase):
    pass


class ProductPhoto(ProductPhotoBase):
    id: int

    class Config:
        from_attributes = True

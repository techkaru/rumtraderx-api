from datetime import datetime
from pydantic import BaseModel


class ProductPriceBase(BaseModel):
    date : datetime
    amount : float
    currency : str
    order_src : str
    order_id : str
    product_id : str


class ProductPriceCreate(ProductPriceBase):
    pass


class ProductPrice(ProductPriceBase):
    id: int

    class Config:
        from_attributes = True


from datetime import datetime
from pydantic import BaseModel


class AskPreview(BaseModel):
    id: int
    image_url: str
    name: str
    brand: str
    price: float
    currency: str
    product_note: float | None = None
    expirated_date: datetime
    is_favorited: bool


class Ask(BaseModel):
    id: int
    status: str
    price: float
    description: str
    expirated_date: datetime
    is_approved: bool
    is_private: bool
    is_bid_linked: bool
    linked_bid: int | None = None
    seller_id: int
    created_date: datetime
    updated_date: datetime


class ProductAskCreate(BaseModel):
    product_id: int
    quantity: int
    is_sample: bool
    sample_size: int | None = None
    bottle_nb: int | None = None


class AskCreate(BaseModel):
    price: float
    description: str
    expirated_date: datetime
    seller_id: int
    products_ask: list[ProductAskCreate]


class ProductAsk(BaseModel):
    id: int
    quantity: int
    is_sample: bool
    is_active: bool
    sample_size: int | None = None
    bottle_nb: int | None = None
    ask_id: int
    product_id: int
    ask: Ask

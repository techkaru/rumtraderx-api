from pydantic import BaseModel
from datetime import datetime


class Bid(BaseModel):
    id: int
    status: str
    max_price: float
    expirated_date: datetime
    is_approved: bool
    buyer_id: int
    created_date: datetime
    updated_date: datetime


class ProductBidCreate(BaseModel):
    product_id: int
    is_sample: bool
    min_sample_size: int | None = None


class BidCreate(BaseModel):
    max_price: float
    expirated_date: datetime
    buyer_id: int
    products_bid: list[ProductBidCreate]


class ProductBid(BaseModel):
    id: int
    is_sample: bool
    min_sample_size: int | None = None
    bid_id: int
    product_id: int
    bid: Bid

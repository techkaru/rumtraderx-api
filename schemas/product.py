from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.ask import ProductAsk
from schemas.bid import ProductBid
from schemas.distillery import Distillery
from schemas.brand import Brand
from schemas.production_method_detail import ProductionMethodDetail 
from schemas.bottler import Bottler 
from schemas.canne_type import CanneType


class ProductBase(BaseModel):
    name: str
    description: str
    category: str
    sku: str | None = None
    made_from: str
    distillation_type: str
    aging_climate: str | None = None
    aging_type: str | None = None
    batch: int | None = None
    abv: float
    size: int
    bottled_year: int | None = None
    year: int | None = None
    age: int | None = None
    total_bottles: int | None = None
    main_picture: str | None = None
    is_single_cask: bool | None = None
    cask_number: str | None = None
    is_bio: bool | None = None
    is_parcellaire: bool | None = None
    is_approved: bool
    is_discontinued: bool
    is_active: bool
    brand: str
    production_method: str
    distillery: str
    bottler: str | None = None
    canne_type: str | None = None
    twelve_month_high: float | None = None
    twelve_month_low: float | None = None
    volatility: float | None = None
    avg_sale_price: float | None = None
    monthly_change: float | None = None
    best_sale_price: float | None = None
    last_buy_ask_price: float | None = None
    country: str
    region: str | None = None
    min_ask_price: float | None = None
    min_ask_id: int | None = None
    max_bid_price: float | None = None
    max_bid_id: int | None = None
    production_method_detail_id: int | None = None
    brand_id: int
    bottler_id: int | None = None
    canne_type_id: int | None = None
    distillery_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    slug: str
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True


class ProductRead(ProductBase):
    id: int
    slug: str
    brand: Brand
    production_method_detail: ProductionMethodDetail | None = None
    bottler: Bottler | None = None
    canne_type: CanneType | None = None
    distillery: Distillery
    product_asks: list[ProductAsk] = []
    product_bids: list[ProductBid] = []
    created_date: datetime
    updated_date: datetime


class ProductList(BaseModel):
    list: list[ProductBase]
    counter: int
    start: int
    limit: int

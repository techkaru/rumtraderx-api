from datetime import datetime
from pydantic import BaseModel
from schemas.ask import AskPreview



class UserFollower(BaseModel):
    user_picture: str
    fullname: str
    username: str

class Message(BaseModel):
    user_picture: str
    username: str
    message_date: str


class ReviewPreview(BaseModel):
    reviewer_name: str
    note: float
    message: str | None = None


class Address(BaseModel):
    name: str
    line_1: str
    line_2: str | None = None
    postal_code: str
    city: str
    state: str
    country: str
    other_details: str | None = None


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    is_active: bool
    username: str | None = None
    category: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    country_code: str | None = None
    phone: str | None = None
    created_date: datetime
    updated_date: datetime | None = None

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass


class UserDashboard(UserBase):
    sales_pending: float
    first_name: str
    user_name: str
    total_sales: float
    total_buys: float
    new_messages: list[Message] #limit 5
    # recently_buy: list[ProductPreview] #limit 4
    # recently_sold: list[ProductPreview] #limit 4
    nb_ask: int
    new_followers: list[UserFollower] #limit 3
    last_reviews: ReviewPreview


class UserProfile(UserBase):
    full_name: str
    user_name: str
    shop_image: str
    shop_banner: str
    avg_note: float | None = None
    total_ask_sales: float
    nb_follower: int | None = None
    is_verified: bool
    # is_popular: bool
    localisation: str
    shop_description: str
    shipping_address: Address
    billing_address: Address
    ask: list[AskPreview] #limit 8
    # credit_card: list[CreditCard]


class UserShop(UserBase):
    shop_name: str
    shop_image: str
    shop_banner: str
    shop_description: str
    is_verified: bool
    # is_popular: bool
    nb_reviews: int | None = None
    avg_note: float | None = None
    reviews: list[ReviewPreview] # limit 4
    nb_active_asks: int
    ask: list[AskPreview]
    

class UserInbox():
    pass

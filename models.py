from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship

from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    sku = Column(String, nullable=True)
    name = Column(String)
    slug = Column(String)
    country = Column(String) ##
    region = Column(String) ##
    description = Column(Text)
    made_from = Column(String) ##
    distillation_type = Column(String) ##
    ## aging_climate = Column(String, nullable=True) ##
    aging_type = Column(String, nullable=True) ##
    batch = Column(Integer, nullable=True)
    canne_type = Column(Integer, nullable=True)
    abv = Column(Float)
    size = Column(Integer)
    bottled_year = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    total_bottles = Column(Integer, nullable=True)
    main_picture = Column(String, nullable=True)
    is_single_cask = Column(String, nullable=True)
    cask_type = Column(String, nullable=True) ##
    cask_number = Column(String, nullable=True)
    is_bio = Column(Boolean, nullable=True)
    is_parcellaire = Column(Boolean, nullable=True)
    is_approved = Column(Boolean, default=False)
    is_discontinued = Column(Boolean, nullable=True)
    is_active = Column(Boolean, default=False)
    production_method = Column(String) ##
    production_method_detail = Column(String, nullable=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    bottler_id = Column(Integer, ForeignKey('bottler.id'))
    distillery_id = Column(Integer, ForeignKey('distillery.id'))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # CALCULATED FIELD
    min_ask_price = Column(Float, nullable=True)
    min_ask_id =  Column(Integer, ForeignKey('ask.id'), nullable=True)
    max_bid_price = Column(Float, nullable=True)
    max_bid_id =  Column(Integer, ForeignKey('bid.id'), nullable=True)
    # STATISTICS
    twelve_month_high = Column(Float, nullable=True)
    twelve_month_low = Column(Float, nullable=True)
    volatility = Column(Float, nullable=True)
    avg_sale_price = Column(Float, nullable=True)
    monthly_change = Column(Float, nullable=True)
    best_sale_price = Column(Float, nullable=True)
    last_buy_ask_price = Column(Float, nullable=True)
    # RELATIONSHIPS
    product_asks = relationship("ProductAsk", back_populates="product")
    product_bids = relationship("ProductBid", back_populates="product")
    brand = relationship("Brand", backref="products")
    bottler = relationship("Bottler", backref="products")
    distillery = relationship("Distillery", backref="products")


class ProductAsk(Base):
    __tablename__ = "product_ask"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    is_sample  = Column(Boolean, default=False)
    sample_size  = Column(Integer, nullable=True)
    bottle_nb  = Column(Integer)
    ask_id = Column(Integer, ForeignKey('ask.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product", back_populates="product_asks")
    ask = relationship("Ask", backref="product_ask")
    is_active = Column(Boolean, default=False)


class Ask(Base):
    __tablename__ = "ask"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    price = Column(Float)
    description = Column(Text)
    expirated_date  = Column(DateTime)
    is_approved = Column(Boolean, default=False)
    is_private = Column(Boolean, default=False)
    is_bid_linked  = Column(Boolean, default=False)
    linked_bid = Column(Integer, ForeignKey('bid.id'), nullable=True)
    seller_id = Column(Integer, ForeignKey('user.id'))
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductBid(Base):
    __tablename__ = "product_bid"

    id = Column(Integer, primary_key=True, index=True)
    is_sample = Column(Boolean)
    min_sample_size = Column(Integer, nullable=True)
    bid_id = Column(Integer, ForeignKey('bid.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product", back_populates="product_bids")
    bid = relationship("Bid", backref="product_bid")
    is_active = Column(Boolean, default=False)


class Bid(Base):
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey('user.id'))
    max_price = Column(Float)
    status = Column(String)
    expirated_date  = Column(DateTime)
    is_approved = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductPhoto(Base):
    __tablename__ = "product_photo"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String)
    url = Column(String)
    product_id = Column(Integer, ForeignKey('product.id'))


class ProductPrice(Base):
    __tablename__ = "product_price"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    amount = Column(Float)
    currency = Column(String)
    order_src = Column(String)
    order_id = Column(String)
    product_id = Column(Integer, ForeignKey('product.id'))


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    line_1 = Column(String)
    line_2 = Column(String, nullable=True)
    postal_code = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    other_details = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))


class ExternalRef(Base):
    __tablename__ = "external_ref"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    external_id = Column(String)
    product_id = Column(Integer, ForeignKey('product.id'))


class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    country = Column(String)
    region = Column(String)


class Distillery(Base):
    __tablename__ = "distillery"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    creation_date = Column(DateTime)
    is_alive  = Column(Boolean)
    closure_date = Column(DateTime, nullable=True)
    country = Column(String)
    region = Column(String, nullable=True)
    owned_by = Column(String, nullable=True)
    city = Column(String)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    website = Column(String, nullable=True)
    coordinates_lon = Column(String, nullable=True)
    coordinates_lat = Column(String, nullable=True)


class Bottler(Base):
    __tablename__ = "bottler"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    country = Column(String)
    region = Column(String)


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    created_at  = Column(DateTime)
    message = Column(Text)
    from_user = Column(Integer, ForeignKey('user.id'))
    ask_id = Column(Integer, ForeignKey('ask.id'))


class AskPhoto(Base):
    __tablename__ = "ask_photos"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String) 
    url = Column(String) 
    ask_id = Column(Integer, ForeignKey('ask.id'))


class AskShippingMethod(Base):
    __tablename__ = "ask_shipping_method"

    id = Column(Integer, primary_key=True, index=True)
    ask_id = Column(Integer, ForeignKey('ask.id'))
    shipping_method_id = Column(Integer, ForeignKey('shipping_method.id'))


class ShippingMethod(Base):
    __tablename__ = "shipping_method"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) 


class UserReview(Base):
    __tablename__ = "user_review"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(Float)
    message = Column(Text)
    ask_id = Column(Integer, ForeignKey('ask.id'))


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey('user.id'))
    status = Column(String) 
    final_price = Column(Float)
    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shipping_address_id = Column(Integer, ForeignKey('address.id'))
    note = Column(Text)
    is_paid  = Column(Boolean)
    created_date = Column(DateTime, default=datetime.utcnow)


class AskOrder(Base):
    __tablename__ = "ask_order"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    order_id = Column(Integer, ForeignKey('order.id'))
    ask_id = Column(Integer, ForeignKey('ask.id'))


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    feedback = Column(Text)
    order_id = Column(Integer, ForeignKey('order.id'))
    created_date = Column(DateTime, default=datetime.utcnow)


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)
    external_source = Column(String) 
    external_id = Column(String) 
    order_id = Column(Integer, ForeignKey('order.id'))
    created_date = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String) 
    username = Column(String, nullable=True) 
    category = Column(String, nullable=True) 
    first_name = Column(String, nullable=True) 
    last_name = Column(String, nullable=True) 
    full_name = Column(String, nullable=True) 
    shop_name = Column(String, nullable=True) 
    shop_image = Column(String, nullable=True) 
    shop_banner = Column(String, nullable=True) 
    shop_description = Column(String, nullable=True) 
    country_code = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=True)
    avg_note = Column(Float)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

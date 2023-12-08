from sqlalchemy.orm import Session

from models import Bid, ProductBid
from schemas.bid import BidCreate


def create_bid(db: Session, bid: BidCreate):
    db_bid = Bid(
        status='pending',
        max_price=bid.max_price,
        expirated_date=bid.expirated_date,
        is_approved=False,
        buyer_id=bid.buyer_id
    )
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)

    for product in bid.products_bid:
        db_product_bid = ProductBid(
            is_sample=product.is_sample,
            min_sample_size=product.min_sample_size,
            product_id=product.product_id,
            bid_id=db_bid.id
        )
        db.add(db_product_bid)
        db.commit()
        db.refresh(db_product_bid)

    return db_bid

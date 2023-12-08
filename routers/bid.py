from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.bid import create_bid
from schemas.bid import Bid, BidCreate


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


BidRouter = APIRouter(
    prefix="/bids",
    tags=["bids"],
)


@BidRouter.post("/", response_model=Bid)
def post_bid(bid: BidCreate, db: Session = Depends(get_db)):
    created_bid = create_bid(db=db, bid=bid)
    return created_bid

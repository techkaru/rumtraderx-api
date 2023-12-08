from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.offer import get_offer_by_email, get_offer
from schemas.offer import Offer, OfferCreate


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


OfferRouter = APIRouter(
    prefix="/offers",
    tags=["offers"],
)


@OfferRouter.get("/", response_model=Offer)
async def get_offer(start: int = 0, limit: int = 10):
    return {"offer_id": "offer_ids"}


@OfferRouter.get("/offers/{offer_id}", response_model=Offer)
async def get_offer(offer_id: int):
    return {"offer_id": offer_id}
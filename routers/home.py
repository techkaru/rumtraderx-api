from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.product import get_product_by_email, get_product
from schemas.product import Product, ProductCreate


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


HomeRouter = APIRouter(
    prefix="/home",
    tags=["home"],
)


# @HomeRouter.post("/", response_model=Product)
# @app.get("/home/")
# async def read_products():
#     return {"home": "home"}
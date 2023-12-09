from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.product import create_product, get_product, get_products
from schemas.product import Product, ProductCreate, ProductRead, ProductList


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ProductRouter = APIRouter(
    prefix="/products",
    tags=["products"],
)


@ProductRouter.post("/", response_model=Product)
def post_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product)
    return db_product


# @ProductRouter.get("/{product_id}", response_model=ProductRead)
@ProductRouter.get("/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@ProductRouter.get("/")
async def read_products(db: Session = Depends(get_db), page: int = 0, page_size: int = 10):
    db_products = get_products(db, page, page_size)
    return db_products

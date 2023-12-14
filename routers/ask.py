from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.ask import create_ask, get_ask
from schemas.ask import Ask, AskCreate
from schemas.product_ask import ProductAskRead


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


AskRouter = APIRouter(
    prefix="/asks",
    tags=["asks"],
)


@AskRouter.post("/", response_model=Ask)
def post_ask(ask: AskCreate, db: Session = Depends(get_db)):
    created_ask = create_ask(db=db, ask=ask)
    return created_ask


@AskRouter.get("/{ask_id}", response_model=ProductAskRead)
def read_ask(ask_id: int, db: Session = Depends(get_db)):
    db_ask = get_ask(db, ask_id=ask_id)
    if db_ask is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_ask

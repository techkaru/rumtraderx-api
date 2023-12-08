from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.ask import create_ask
from schemas.ask import Ask, AskCreate


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

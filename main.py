from fastapi import FastAPI
from sqlalchemy.orm import Session

from database import engine
import models
from routers.ask import AskRouter
from routers.bid import BidRouter
from routers.users import UserRouter
from routers.products import ProductRouter


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ProductRouter)
app.include_router(UserRouter)
app.include_router(AskRouter)
app.include_router(BidRouter)


# @app.get("/")
# def read_root():
#     return {"message": "It's working!"}

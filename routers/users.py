from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal

from crud.user import get_user_by_email, get_user, create_user
from schemas.user import User, UserCreate, UserDashboard, UserShop, UserProfile


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


UserRouter = APIRouter(
    prefix="/users",
    tags=["users"],
)


@UserRouter.post("/", response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@UserRouter.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@UserRouter.get("/me")
async def read_user_me():
    return {"user_id": "the current user"}


@UserRouter.get("/{user_id}/dashboard/", response_model=UserDashboard)
async def read_products(user_id: int):
    return {"product_id": user_id}


@UserRouter.get("/{user_id}/profile/", response_model=UserProfile)
async def read_profile(user_id: int):
    return {"user_id": user_id}


@UserRouter.get("/{user_id}/shop", response_model=UserShop)
async def read_shop(user_id: int, start: int = 0, limit: int = 10):
    return {"shop_id": user_id}


# @UserRouter.get("/{user_id}/inbox", response_model=UserInbox)
# async def read_shop(user_id: int, start: int = 0, limit: int = 10):
#     return {"shop_id": user_id}


# @UserRouter.get("/{user_id}/inbox/{other_user_id}")
# async def read_shop(user_id: int, other_user_id: int, start: int = 0, limit: int = 10):
#     return {
#         "user_1": user_id,
#         "user_2": other_user_id
#     }
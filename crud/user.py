from sqlalchemy.orm import Session

from models import User
from schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_user_dashboard(db: Session, user_id: int):
#     user_dashboard = db.query(User).\
#         filter(Product.id == product_id).\
#         join(Product.brand).\
#         join(Product.production_method_detail).\
#         join(Product.bottler).\
#         join(Product.canne_type).\
#         join(Product.distillery).\
#         join(Product.region).\
#         first()
#     return user_dashboard
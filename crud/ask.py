from sqlalchemy.orm import Session

from models import Ask, ProductAsk
from schemas.ask import AskCreate


def create_ask(db: Session, ask: AskCreate):
    db_ask = Ask(
        status='pending',
        price=ask.price,
        description=ask.description,
        expirated_date=ask.expirated_date,
        is_private=False,
        seller_id=ask.seller_id
    )
    db.add(db_ask)
    db.commit()
    db.refresh(db_ask)

    for product in ask.products_ask:
        db_product_ask = ProductAsk(
            quantity=product.quantity,
            is_sample=product.is_sample,
            sample_size=product.sample_size,
            bottle_nb=product.bottle_nb,
            product_id=product.product_id,
            ask_id=db_ask.id
        )
        db.add(db_product_ask)
        db.commit()
        db.refresh(db_product_ask)

    return db_ask


def get_ask(db: Session, ask_id: int):
    return db.query(ProductAsk
        ).filter(ProductAsk.is_active == True
        ).filter(ProductAsk.ask_id == ask_id
        ).join(ProductAsk.ask
        ).join(ProductAsk.product
        ).first()

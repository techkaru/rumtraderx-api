from sqlalchemy.orm import Session

from models import ProductPhoto
from schemas.product_photo import ProductPhotoCreate


def create_product_photo(db: Session, product_photo: ProductPhotoCreate):
    db_product_photo = ProductPhoto(
        external_id=product_photo.external_id,
        url=product_photo.url,
        product_id=product_photo.product_id,
    )
    db.add(db_product_photo)
    db.commit()
    db.refresh(db_product_photo)
    return db_product_photo


def get_product_photo(db: Session, product_photo_id: int):
    return db.query(ProductPhoto).filter(ProductPhoto.id == product_photo_id).first()

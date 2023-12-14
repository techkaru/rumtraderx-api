from models import Product, ProductAsk, ProductBid
from schemas.product import ProductCreate, ProductList
from slugify import slugify
from sqlalchemy.orm import Session


def get_products(db: Session, page: int, page_size: int):
    db_products = db.query(Product
        ).filter(Product.is_approved == True
        ).limit(page_size
        ).offset(page*page_size
        ).all()

    return db_products


def get_product(db: Session, product_id: int):
    product = db.query(Product
        ).filter(Product.id == product_id
        ).join(Product.brand
        ).join(Product.bottler
        ).join(Product.distillery
        ).first()

    if product:
        product.product_asks = db.query(ProductAsk
            ).filter(ProductAsk.product_id == product_id
            ).filter(ProductAsk.is_active == True
            ).all()
        
        product.product_bids = db.query(ProductBid
            ).filter(ProductBid.product_id == product_id
            ).filter(ProductBid.is_active == True
            ).all()

    return product


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        category=product.category,
        sku=product.sku,
        name=product.name,
        slug=slugify(product.name),
        description=product.description,
        made_from=product.made_from,
        distillation_type=product.distillation_type,
        aging_climate=product.aging_climate,
        aging_type=product.aging_type,
        batch=product.batch,
        abv=product.abv,
        size=product.size,
        canne_type=product.canne_type,
        bottled_year=product.bottled_year,
        year=product.year,
        age=product.age,
        total_bottles=product.total_bottles,
        main_picture=product.main_picture,
        is_single_cask=product.is_single_cask,
        cask_number=product.cask_number,
        is_bio=product.is_bio,
        is_parcellaire=product.is_parcellaire,
        is_approved=product.is_approved,
        is_discontinued=product.is_discontinued,
        production_method=product.production_method,
        is_active=product.is_active,
        production_method_detail=product.production_method_detail,
        brand_id=product.brand_id,
        bottler_id=product.bottler_id,
        distillery_id=product.distillery_id,
        region=product.region,
        country=product.country
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

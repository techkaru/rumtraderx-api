from pydantic import BaseModel
from schemas.ask import Ask
from schemas.ask import ProductAskBase
from schemas.product import ProductRead

class ProductAskRead(ProductAskBase):
    ask: Ask
    product: ProductRead

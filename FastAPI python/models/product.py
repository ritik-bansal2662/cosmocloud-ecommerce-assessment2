from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float = 0.00
    qty: int = 0
from pydantic import BaseModel

class Order(BaseModel):
    items: list[dict]
    amount: int
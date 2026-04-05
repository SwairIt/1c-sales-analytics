from pydantic import BaseModel

class SaleItem(BaseModel):
    order_id: int
    amount: int
    date: str
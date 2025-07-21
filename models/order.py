from pydantic import BaseModel, Field
from typing import List, Optional


class Items(BaseModel):
    productId: str
    qty: int


class Orders(BaseModel):
    userId: Optional[str] = "user_1"
    items: List[Items] = Field(..., min_items=1)

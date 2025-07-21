from pydantic import BaseModel, Field
from typing import List


class Sizes(BaseModel):
    size: str
    quantity: int


class Products(BaseModel):
    name: str
    price: int
    sizes: List[Sizes] = Field(..., min_items=1)

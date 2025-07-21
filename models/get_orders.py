from pydantic import BaseModel
from typing import Optional


class OrderFilters(BaseModel):
    limit: Optional[int] = 0
    offset: Optional[int] = 0

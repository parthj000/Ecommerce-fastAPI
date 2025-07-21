from pydantic import BaseModel
from typing import Optional

class ProductFilters(BaseModel):
    name:Optional[str] = ""
    size:Optional[str] = ""
    limit:Optional[int] = 0
    offset:Optional[int] = 0
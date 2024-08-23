from pydantic import BaseModel
from typing import Optional
from datetime import date

class Category(BaseModel):
    id: Optional[int] = None
    name: str
    is_active: bool
    created_at : date
    posther_path: Optional[str]= None
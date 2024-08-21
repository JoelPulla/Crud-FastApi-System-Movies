from pydantic import Field, BaseModel
from typing import Optional


class CategoryTvSchema(BaseModel):
    
    id: Optional[int] = None
    name: str
    description: str
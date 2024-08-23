from pydantic import BaseModel
from typing import Optional

class Tv(BaseModel):    
    
    id: Optional[ int]  = None
    name : str
    image_url: str
    info : str
    url_stream : str
    country: str
    category: str
    is_active : bool
    
    
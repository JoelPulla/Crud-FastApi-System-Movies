from pydantic import BaseModel
from typing import Optional
from datetime import date

class Movie(BaseModel):
    
    id : Optional[int] = None
    movie_title  : str
    overview : str
    id_tmdb : Optional[int]= None
    url_video : str
    is_youtube  : bool
    poster_path  : str
    background_path  : str
    voute_range  : float
    popularity  : float
    created_at  : date
    release  : date
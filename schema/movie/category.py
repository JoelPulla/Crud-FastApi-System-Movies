from pydantic import BaseModel
from typing import Optional, List
from datetime import date



#Schema para crear un categoria
class CategoryCreate(BaseModel):
    name: str
    is_active: bool
    created_at : date
    posther_path: Optional[str]= None
    
# Schema para devolver una categoria
class Category(BaseModel):
    id: int
    name: str
    is_active: bool
    created_at : date
    posther_path: Optional[str]= None
    class Config:
        orm_mode = True
        
# Schema para crear una pelicula
class MovieCreate(BaseModel):
    
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
    category_ids: List[int]  # Lista de IDs de categorías

    class Config:
        orm_mode = True
    

# Schema para devolver una movie
class Movie(BaseModel):
    
    id: Optional[int] = None
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
    categories: List[Category] = []
    
    class Config:
        orm_mode = True
    
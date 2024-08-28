from config.db import Base
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship
from models.movie.movie_category import MovieCategory


class CategoryModel(Base):
    
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at= Column(Date)
    posther_path = Column(String)
    
    
    # Relacion con Categorias
    movies =  relationship("MovieCategory",  back_populates="category")
    
    
    
    
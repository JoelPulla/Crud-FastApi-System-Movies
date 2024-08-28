from config.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Table, String, Boolean, Double, Date
from sqlalchemy.orm import relationship


#Table pivote Movie - Category

movie_category = Table( "movie_category", Base.metadata,
    
    Column("movie_id", ForeignKey("movie.id"), primary_key=True),
    Column("category_id", ForeignKey("category.id"), primary_key=True),
)
        

class MovieModel(Base):
    
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    overview= Column(String)
    id_tmdb = Column(Integer)
    url_video= Column(String)
    is_youtube = Column(Boolean)
    poster_path = Column(String)
    background_path = Column(String)
    voute_range = Column(Double)
    popularity = Column(Double)
    created_at = Column(Date)
    release = Column(Date)
    #relacion con Category
    categories = relationship("CategoryModel", secondary= "movie_category", back_populates="movies" )

class CategoryModel(Base):
    
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at= Column(Date)
    posther_path = Column(String)
    # Relacion con Categorias
    movies =  relationship("MovieModel", secondary= "movie_category",  back_populates="categories")
    
    
    
    
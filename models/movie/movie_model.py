from config.db import Base
from sqlalchemy import Column, Integer, String, Boolean, Double, Date
from sqlalchemy.orm import relationship
from models.movie.movie_category import MovieCategory

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
    
    
    """Relacion con categoria"""
    categories = relationship("MovieCategory",back_populates="movie" )
from config.db import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


"""Table pivote Movie - Category"""


class MovieCategory(Base):
    __tablename__ = 'movie_category'
    
    movie_id = Column(Integer, ForeignKey('movie.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)

    # Relaciones
    movie = relationship('MovieModel', back_populates='categories')  # Corregido la referencia a 'categories'
    category = relationship('CategoryModel', back_populates='movies')





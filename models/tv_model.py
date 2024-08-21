from config.db import Base
from sqlalchemy import Column, Integer, String, Boolean


class TvModel(Base):    
    __tablename__ = "tv"
    id = Column(Integer, primary_key= True)
    name = Column(String)
    image_url = Column(String)
    info = Column(String)
    url_stream = Column(String)
    country = Column(String)
    categoty = Column(Integer)
    is_active = Column(Boolean)
    
    
    
    
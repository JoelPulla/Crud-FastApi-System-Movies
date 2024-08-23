from config.db import Base
from sqlalchemy import String, Integer, Boolean, Column


class CategoryTv(Base):
    
    __tablename__ = 'categorytv'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
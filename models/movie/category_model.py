from config.db import Base
from sqlalchemy import Column, String, Integer, Boolean, Date

class CategoryModel(Base):
    
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_active = Column(Boolean)
    created_at= Column(Date)
    posther_path = Column(String)
    
    
    
    
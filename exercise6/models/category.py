from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100), nullable = False, unique = True)

    products = relationship('Product', back_populates = 'category')

    def __repr__(self):
        return f"\n<Product -> ID = {self.category_id} | '{self.name}'>\n"
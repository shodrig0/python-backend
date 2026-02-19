from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String(250), nullable = False)
    sku = Column(String(50), nullable = False)
    stock = Column(Integer, nullable = False)
    branch_id = Column(Integer, ForeignKey('branch.branch_id'))
    
    branch = relationship('Branch', back_populates = 'products')
    prices = relationship('Price', back_populates = 'product')

    def __repr__(self):
        return f"<Product(title='{self.description}', sku='{self.sku}', stock='{self.stock}')>"
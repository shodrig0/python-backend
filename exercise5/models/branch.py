from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Branch(Base):
    __tablename__ = 'branch'

    branch_id = Column(Integer, primary_key = True, autoincrement = True)
    city = Column(String(100), nullable = False)
    postal_code = Column(String(100), nullable = False)

    products = relationship('Product', back_populates = 'branch')
    prices = relationship('Price', back_populates = 'branch')

    def __repr__(self):
        return f"<Branch(city='{self.city}', postal_code='{self.postal_code}', products={self.products})>"
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String(250), nullable = False)
    sku = Column(String(50), nullable = False, unique = True)

    # prices = relationship('Price', back_populates = 'product')
    product_branches = relationship('ProductBranch', back_populates = 'product')

    __table_args__ = (UniqueConstraint('sku', name = 'uq_product_sku'),)
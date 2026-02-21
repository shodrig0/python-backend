from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String(250), nullable = False)
    sku = Column(String(50), nullable = False, unique = True)

    product_branches = relationship('ProductBranch', cascade = 'all, delete', back_populates = 'product')

    __table_args__ = (UniqueConstraint('sku', name = 'uq_product_sku'),)

    def __repr__(self):
        return f"\n<Product -> ID = {self.product_id} | '{self.description}' | SKU = '{self.sku}'>\n"
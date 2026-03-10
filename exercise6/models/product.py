from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key = True, autoincrement = True) # <- internal db id

    sku = Column(String(50), nullable = False, unique = True) # <- fakestore id product
    title = Column(String(100), nullable = False)
    description = Column(String(250), nullable = False)
    image = Column(String(100), nullable = True)

    category_id = Column(ForeignKey('category.category_id'), nullable = False)

    product_branches = relationship('ProductBranch', cascade = 'all, delete', back_populates = 'product')
    category = relationship('Category', back_populates = 'products')

    __table_args__ = (UniqueConstraint('sku', name = 'uq_product_sku'),)

    def __repr__(self):
        return f"\n<Product -> ID = {self.product_id} | Title = '{self.title}' | Description = '{self.description}' | SKU = '{self.sku}' | Image = '{self.image}'>\n"
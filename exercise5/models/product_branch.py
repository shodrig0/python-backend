from sqlalchemy import ForeignKey, Integer, Column
from sqlalchemy.orm import relationship
from .base import Base

class ProductBranch(Base):
    __tablename__ = 'product_branch'

    branch_id = Column(ForeignKey('branch.branch_id'), primary_key = True)
    product_id = Column(ForeignKey('product.product_id'), primary_key = True)
    
    stock = Column(Integer, nullable = False)

    branch = relationship('Branch', back_populates = 'product_branches')
    product = relationship('Product', back_populates = 'product_branches')
    prices = relationship('Price', back_populates = 'product_branch')
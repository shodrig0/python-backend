from sqlalchemy import ForeignKey, Integer, Column, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class ProductBranch(Base):
    __tablename__ = 'product_branch'

    product_branch_id = Column(Integer, primary_key = True, autoincrement = True)

    branch_id = Column(ForeignKey('branch.branch_id'), nullable = False)
    product_id = Column(ForeignKey('product.product_id'), nullable = False)
    
    stock = Column(Integer, nullable = False)

    __table_args__ = (UniqueConstraint('branch_id', 'product_id'), )

    branch = relationship('Branch', back_populates = 'product_branches')
    product = relationship('Product', back_populates = 'product_branches')
    prices = relationship('Price', back_populates = 'product_branch')
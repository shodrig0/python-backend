from sqlalchemy import Column, Integer, TIMESTAMP, DECIMAL, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Price(Base):
    __tablename__ = 'price'

    price_id = Column(Integer, primary_key = True, autoincrement = True)
    amount = Column(DECIMAL(100, 2), nullable = False)
    valid_from = Column(TIMESTAMP(timezone = True), nullable = False)
    valid_to = Column(TIMESTAMP(timezone = True), nullable = True)

    product_id = Column(Integer, nullable = False)
    branch_id = Column(Integer, nullable = False)

    __table_args__ = (ForeignKeyConstraint(['branch_id', 'product_id'], ['product_branch.branch_id', 'product_branch.product_id']),)

    product_branch = relationship('ProductBranch', back_populates = 'prices')
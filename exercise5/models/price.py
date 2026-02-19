from sqlalchemy import Column, Integer, TIMESTAMP, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class Price(Base):
    __tablename__ = 'price'

    price_id = Column(Integer, primary_key = True, autoincrement = True)
    amount = Column(DECIMAL(100, 2), nullable = False)
    date = Column(TIMESTAMP(timezone = True), server_default = func.now(), nullable = False)

    product_id = Column(Integer, ForeignKey('product.product_id'))
    branch_id = Column(Integer, ForeignKey('branch.branch_id'))

    product = relationship('Product', back_populates = 'prices')
    branch = relationship('Branch', back_populates = 'prices')
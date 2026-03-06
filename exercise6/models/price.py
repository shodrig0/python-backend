from sqlalchemy import Column, Integer, TIMESTAMP, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Price(Base):
    __tablename__ = 'price'

    price_id = Column(Integer, primary_key = True, autoincrement = True)
    amount = Column(DECIMAL(100, 2), nullable = False)
    valid_from = Column(TIMESTAMP(timezone = True), nullable = False)
    valid_to = Column(TIMESTAMP(timezone = True), nullable = True)

    product_branch_id = Column(ForeignKey('product_branch.product_branch_id'), nullable = False)

    product_branch = relationship('ProductBranch', back_populates = 'prices')

    def __repr__(self):
        return f"\n<Price -> ID = {self.price_id} | $'{self.amount}' | VALID FROM = '{self.valid_from}' | VALID TO = '{self.valid_to}'>\n"
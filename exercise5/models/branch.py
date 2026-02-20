from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Branch(Base):
    __tablename__ = 'branch'

    branch_id = Column(Integer, primary_key = True, autoincrement = True)
    city = Column(String(100), nullable = False)
    postal_code = Column(String(100), nullable = False)

    product_branches = relationship('ProductBranch', back_populates = 'branch')

    def __repr__(self):
        return f"\n<Branch -> ID = {self.branch_id} | '{self.city}' | POSTAL CODE = '{self.postal_code}'>\n"
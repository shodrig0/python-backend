from sqlalchemy import Column, Integer, String, DECIMAL
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from config.engine import engine
from .base import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key = True, autoincrement = True)
    description = Column(String(250), nullable = False)
    price = Column(DECIMAL(precision = 10, scale = 2), nullable = False)
    region = Column(String(100), nullable = False)
    sku = Column(String(50), nullable = False)
    stock = Column(Integer, nullable = False)

    def __repr__(self):
        return f"<Product(title='{self.description}', price='{self.price}', region='{self.region}', sku='{self.sku}', stock='{self.stock}')>"
    
# Base.metadata.create_all(engine)

# session = Session()

# new_product = Product(description = "Chocolate", price = 10.5, region = "Kansas", sku = "1211", stock = 100)
# session.add(new_product)
# session.commit()

# product = session.query(Product).filter_by(description = "Milk")
# print(product)

# session.close()
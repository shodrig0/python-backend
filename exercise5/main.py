from config.engine import engine, SessionLocal
from models.base import Base
from models.product import Product

def init_db():
    Base.metadata.create_all(engine)

def main():
    init_db()

    session_db = SessionLocal()

    new_product = Product(description = "Watermelon Sugar", price = 65, region = "Toronto", sku = "33214", stock = 50)
    session_db.add(new_product)
    session_db.commit()


if __name__ == "__main__":
    main()
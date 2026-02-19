from config.engine import engine, SessionLocal
from models.base import Base
from models.branch import Branch
from models.price import Price
from models.product import Product

def init_db():
    Base.metadata.create_all(engine)

def main():
    init_db()

    session_db = SessionLocal()
    session_db.commit()
    session_db.close()

if __name__ == "__main__":
    main()
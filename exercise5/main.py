from config.engine import engine, SessionLocal
from models.base import Base
from models.branch import Branch
from models.price import Price
from models.product import Product
from models.product_branch import ProductBranch
from datetime import datetime, timezone

def init_db():
    Base.metadata.create_all(engine)

def main():
    init_db()

    session_db = SessionLocal()

    new_branch = Branch(city = 'NY', postal_code = 'NY-123')
    new_product = Product(description = 'Watermelon Sugar', sku = '12345')
    new_product_branch = ProductBranch(product = new_product, branch = new_branch, stock = 120)
    new_price = Price(amount = 20.5, valid_from = datetime.now(timezone.utc), valid_to = None, product_branch = new_product_branch)

    session_db.add_all([new_branch, new_product, new_product_branch, new_price])

    session_db.commit()
    session_db.close()

    print('Done')

if __name__ == '__main__':
    main()
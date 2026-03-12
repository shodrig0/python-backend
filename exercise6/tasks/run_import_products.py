from config.engine import SessionLocal
from utils.fakestore_scraper import fakestore_scraper
from services.fakestore import import_products

def run_import_products():
    session = SessionLocal()

    try:
        products = fakestore_scraper("https://fakestoreapi.com/products")
        import_products(session, products)

    finally:
        session.close()
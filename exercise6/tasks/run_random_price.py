from config.engine import SessionLocal
from services.update_price import update_price

def run_random_price():
    session = SessionLocal()

    try:
        update_price(session)
    finally:
        session.close()
from config.engine import engine
from config.engine import SessionLocal
from models.base import Base

def initializer():
    Base.metadata.create_all(engine)

session = SessionLocal()
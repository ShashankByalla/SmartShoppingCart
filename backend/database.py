from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///shopping_cart.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_database():
    from models import Base
    Base.metadata.create_all(engine)

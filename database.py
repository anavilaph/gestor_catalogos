from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///productos.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
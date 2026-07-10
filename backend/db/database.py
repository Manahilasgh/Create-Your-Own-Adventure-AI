from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from core.config import settings

engine = create_engine( settings.DATABASE_URL )
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind = engine)
from sqlalchemy import Column, String, Integer, Boolean
from db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    hash_password = Column(String)
    isVerified = Column(Boolean, default=False)
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    band = Column(String, index=True)

class Phrase(Base):
    __tablename__ = 'phrases'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, unique=True, index=True)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    country = Column(String, index=True)
    timezone = Column(String, index=True)

def init_db():
    Base.metadata.create_all(bind=engine)
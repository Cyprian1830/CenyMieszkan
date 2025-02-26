from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'ceny_mieszkań'  # Jeśli tabela jest w schemacie 'dbo', dodaj __table_args__
    __table_args__ = {'schema': 'dbo'}

    id = Column(Integer, primary_key=True, autoincrement=True)  # Klucz główny
    city = Column(String(100), nullable=False)  # Ograniczenie do 100 znaków
    squareMeters = Column(Float, nullable=False)
    rooms = Column(String(10), nullable=False)
    floor = Column(String(10), nullable=True)
    buildYear = Column(String(10), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    price = Column(Integer, nullable=False)


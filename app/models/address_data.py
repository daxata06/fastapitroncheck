from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Float, Integer, String


class Base(DeclarativeBase):
    pass


class AddressData(Base):
    __tablename__ = "address_data"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    balance = Column(Float)
    bandwidth = Column(Float)
    energy = Column(Float)

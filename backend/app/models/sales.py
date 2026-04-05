from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Sale(Base):
    __tablename__ = "sales"
    order_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    date = Column(String)
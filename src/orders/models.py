from pydantic import BaseModel
from datetime import datetime

from config.databases import Base
from sqlalchemy import Column, Integer, DateTime


class Order(BaseModel):
    id: int
    customer_id: int
    order_date: datetime
    total_amount: int

    class Config:
        from_attributes = True


class OrderDB(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    order_date = Column(DateTime)
    total_amount = Column(Integer)

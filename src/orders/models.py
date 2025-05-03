from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    id: int
    customerId: int
    orderDate: datetime
    totalAmount: int
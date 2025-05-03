from datetime import datetime
from orders.models import Order


def get_order_by_id(order_id: int) -> Order:
    return Order(id=order_id, customerId=1, orderDate=datetime.now(), totalAmount=10)

from datetime import datetime
from orders.models import Order
from orders.telemetries import tracer


def get_order_by_id(order_id: int) -> Order:
    with tracer.start_as_current_span("get-order-by-id-span"):
        return Order(
            id=order_id, customerId=1, orderDate=datetime.now(), totalAmount=10
        )

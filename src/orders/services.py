from orders.models import Order, OrderDB
from orders.telemetries import tracer
from fastapi import HTTPException


def get_order_by_id(order_id: int, db):
    with tracer.start_as_current_span("get-order-by-id-span"):
        order = db.query(OrderDB).filter(OrderDB.id == order_id).first()
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        # return Order.from_orm(order)
        return Order.model_validate(order)

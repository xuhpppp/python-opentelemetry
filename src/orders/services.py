from orders.models import Order, OrderDB
from fastapi import HTTPException
from sqlalchemy import select
from orders.telemetries import tracer


def get_order_by_id(order_id: int, db):
    with tracer.start_as_current_span("service.get_order_by_id"):
        # build the query
        query = select(OrderDB).where(OrderDB.id == order_id)
        with tracer.start_as_current_span("db.query_order_by_id") as span:
            span.set_attribute("db.system", "postgresql")
            span.set_attribute("db.statement", str(query))

            # execute the query
            order = db.execute(query).scalar_one_or_none()
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")

        # return Order.from_orm(order)
        return Order.model_validate(order)

from fastapi import APIRouter, Depends
from orders.models import Order
from orders.services import get_order_by_id
from config.databases import get_db
from sqlalchemy.orm import Session
from orders.telemetries import tracer

router = APIRouter()


@router.get("/orders/{id}", response_model=Order)
def get_order_by_id_router(id: int, db: Session = Depends(get_db)):
    with tracer.start_as_current_span("get-order-by-id-span"):
        return get_order_by_id(id, db=db)

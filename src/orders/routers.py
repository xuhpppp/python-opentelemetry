from fastapi import APIRouter
from orders.models import Order
from orders.services import get_order_by_id

router = APIRouter()


@router.get("/orders/{id}", response_model=Order)
def get_order_by_id_router(id: int):
    return get_order_by_id(id)

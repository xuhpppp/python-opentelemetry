from fastapi import FastAPI
from orders.routers import router as order_router

app = FastAPI()
app.include_router(order_router)

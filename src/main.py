import os
from fastapi import FastAPI, Request
from orders.routers import router as order_router

from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.metrics import set_meter_provider, get_meter_provider
from prometheus_client import make_asgi_app

# Set up the Prometheus exporter
reader = PrometheusMetricReader()
provider = MeterProvider(metric_readers=[reader])
set_meter_provider(provider)
meter = get_meter_provider().get_meter("order-service")

# define counter metric
request_counter = meter.create_counter(
    name="http_requests_total", description="Total number of HTTP requests"
)


app = FastAPI()
app.include_router(order_router)


@app.middleware("http")
async def count_requests(request: Request, call_next):
    response = await call_next(request)
    route = request.url.path
    method = request.method
    status_code = response.status_code
    # does this return to zero after restart?
    # yes, but why do you need to store it persistent?
    # just count the number of requests in a period of time
    request_counter.add(1, attributes={"route": route, "method": method, "status_code": str(status_code)})

    return response

app.mount("/metrics", make_asgi_app())

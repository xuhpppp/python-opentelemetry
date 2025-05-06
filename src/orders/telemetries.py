import os

from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Setup Tracer Provider with Console Exporter
resource = Resource(attributes={SERVICE_NAME: "order-service"})
provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(
    endpoint=os.getenv("OTEL_EXPORTER_JAEGER_ENDPOINT"), insecure=True
)
# processor = BatchSpanProcessor(ConsoleSpanExporter())
processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Create Tracer
tracer = trace.get_tracer(__name__)

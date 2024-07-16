# Set up Azure Monitor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
import logging
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry._logs import set_logger_provider
from dotenv import load_dotenv
import os
# Instrument Django
from opentelemetry.instrumentation.django import DjangoInstrumentor
DjangoInstrumentor().instrument()
from opentelemetry.instrumentation.requests import RequestsInstrumentor  # noqa: E402
RequestsInstrumentor().instrument()

load_dotenv()

# SET UP CONNECTION STRING
APPLICATIONINSIGHTS_CONNECTION_STRING = os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')  # noqa: E501

# Create a Resource object with the cloud.role attribute

# SET UP TRACE EXPORTER
trace_exporter = AzureMonitorTraceExporter(
    connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
)
resource = Resource(attributes={"cloud.role": "DjangoApplication", "service.name": "DjangoApplication"})  # noqa: E501
tracer_provider = TracerProvider(resource=resource)
tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer(__name__)


# SET UP LOGGING EXPORTER
logger_provider = LoggerProvider()
set_logger_provider(logger_provider)

exporter = AzureMonitorLogExporter(
    connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))

# Attach LoggingHandler to namespaced logger
handler = LoggingHandler()
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

from logging_service.models import  RequestTracingModel
from metrics_service.service import MetricsService
from opentelemetry.trace import Span

class LoggingService:
    def __init__(self):
        pass
    
    @staticmethod
    async def save_otel_request_data(data: RequestTracingModel, tracer:Span ):
        tracer.set_attribute("http.url", data.url)
        tracer.set_attribute("http.method", data.method)
        tracer.set_attribute("http.headers", data.headers_str)
        tracer.set_attribute("http.body", data.body_str)
        tracer.set_attribute("http.response", data.response_str)
        tracer.set_attribute("http.status_code", data.status_code)
        tracer.set_attribute("http.duration", data.duration_in_second)

        MetricsService.request_counter.labels(method = data.method, endpoint=data.url, status_code=data.status_code).inc()

        

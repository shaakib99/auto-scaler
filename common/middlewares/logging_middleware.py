from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from fastapi.responses import Response
from datetime import datetime
from opentelemetry import trace
from logging_service.service import LoggingService
from logging_service.models import RequestTracingModel
import json

tracer = trace.get_tracer("auto_scaler.tracer")

class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):       

        with tracer.start_as_current_span(f"[{request.method.upper()}] {request.url.path}") as req_tracer:
            req_start_time = datetime.now()
            
            result = await call_next(request)

            body = b"".join([chunk async for chunk in result.body_iterator])
            response = body.decode('utf-8')

            request_tracing_model = RequestTracingModel()
            request_tracing_model.url = request.base_url.path
            request_tracing_model.method = request.method.upper()
            request_tracing_model.headers_str = json.dumps(dict(request.headers))
            request_tracing_model.body_str = json.dumps(request.body.__dict__ if request.method.lower() != 'get' else {})
            request_tracing_model.response_str = response
            request_tracing_model.status_code = result.status_code
            request_tracing_model.duration_in_second = (datetime.now() - req_start_time).seconds
            await LoggingService.save_otel_request_data(request_tracing_model, req_tracer)

            return Response(
                content=response,
                status_code=result.status_code,
                headers=dict(result.headers),
                media_type=result.media_type,
            )


from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from datetime import datetime
from opentelemetry import trace
from logging_service.service import LoggingService
from logging_service.models import RequestTracingModel
import json

tracer = trace.get_tracer("auto_scaler.tracer")

class ResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.response_template = {
            "status_code": None,
            "data": None,
            "message": None
        }

    async def dispatch(self, request: Request, call_next):
        with tracer.start_as_current_span(f"[{request.method.upper()}] {request.base_url.path}") as req_tracer:
            req_start_time = datetime.now()
            try:
                result = await call_next(request)
                body = b""
                async for chunk in result.body_iterator:
                    body += chunk
                body_text = body.decode("utf-8")
                self.response_template["data"] = json.loads(body_text) if body_text else None

                self.response_template["status_code"] = result.status_code
            except Exception as e:
                if isinstance(e, HTTPException):
                    self.response_template["status_code"] = e.status_code
                    self.response_template["message"] = e.message
                else:
                    self.response_template["status_code"] = 500
                    self.response_template["message"] = e.__str__()

            request_tracing_model = RequestTracingModel()
            request_tracing_model.url = request.base_url.path
            request_tracing_model.method = request.method.upper()
            request_tracing_model.headers_str = json.dumps(dict(request.headers))
            request_tracing_model.body_str = json.dumps(request.body.__dict__ if request.method.lower() != 'get' else {})
            request_tracing_model.response_str = json.dumps(self.response_template)
            request_tracing_model.status_code = self.response_template["status_code"]
            request_tracing_model.duration_in_second = (datetime.now() - req_start_time).seconds
            await LoggingService.save_otel_request_data(request_tracing_model, req_tracer)


            
                    
            return JSONResponse(content=self.response_template, status_code=self.response_template["status_code"])


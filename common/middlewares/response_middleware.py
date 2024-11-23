from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from opentelemetry import trace
import json
import re

tracer = trace.get_tracer("auto_scaler.tracer")

class ResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, excluded_paths: list[str] = []):
        super().__init__(app)
        self.excluded_paths = excluded_paths
        self.response_template = {
            "status_code": None,
            "data": None,
            "message": None
        }

    async def dispatch(self, request: Request, call_next):   
        for excluded_path_pattern in self.excluded_paths:
            if re.match(excluded_path_pattern, request.url.path):
                return await call_next(request)      

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

        return JSONResponse(content=self.response_template, status_code=self.response_template["status_code"])


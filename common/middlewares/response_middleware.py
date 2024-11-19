from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from datetime import datetime
import json

class ResponseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.response_template = {
            "status_code": None,
            "data": None,
            "message": None
        }

    async def dispatch(self, request: Request, call_next):
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
        req_duration = datetime.now() - req_start_time
        
                
        return JSONResponse(content=self.response_template, status_code=self.response_template["status_code"])


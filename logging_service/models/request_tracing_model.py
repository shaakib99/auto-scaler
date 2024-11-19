from pydantic import BaseModel, Field
from typing import Optional

class RequestTracingModel(BaseModel):
    url:Optional[str] = Field(default=None)
    method:Optional[str] = Field(default=None)
    headers_str:Optional[str] = Field(default=None)
    body_str:Optional[str] = Field(default=None)
    response_str:Optional[str] = Field(default=None)
    status_code:Optional[int] = Field(default=None)
    duration_in_second:Optional[float] = Field(default=None)

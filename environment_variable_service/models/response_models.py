from pydantic import BaseModel, Field
from typing import Optional

class ResponseEnvironmentVariableModel(BaseModel):
    worker_id: Optional[int | str] = Field(default=None)
    key: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
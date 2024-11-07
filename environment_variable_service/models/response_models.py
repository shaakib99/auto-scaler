from pydantic import BaseModel, Field
from typing import Optional

class ResponseEnvironmentVariableModel(BaseModel):
    key: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
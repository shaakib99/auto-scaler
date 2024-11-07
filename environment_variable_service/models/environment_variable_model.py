from pydantic import BaseModel, Field
from typing import Optional

class EnvironmentVariableModel(BaseModel):
    key: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
    is_active = Optional[bool] = Field(default=True)
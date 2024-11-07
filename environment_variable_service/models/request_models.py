from pydantic import BaseModel, Field
from typing import Optional

class CreateEnvironmentVariableModel(BaseModel):
    key: str
    value: str

class UpdateEnvironmentVariableModel(BaseModel):
    key: Optional[str]
    value: Optional[str]
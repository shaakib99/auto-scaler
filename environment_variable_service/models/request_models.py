from pydantic import BaseModel
from typing import Optional

class CreateEnvironmentVariableModel(BaseModel):
    worker_id: int
    key: str
    value: str

class UpdateEnvironmentVariableModel(BaseModel):
    key: Optional[str]
    value: Optional[str]
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkerResponseModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    status: Optional[str]
    ram: Optional[int]
    cpu: Optional[int]
    created_at: Optional[datetime]
    update_at: Optional[datetime]
    ports: Optional[list[str]]
    environment_variables = Optional[list[str]]
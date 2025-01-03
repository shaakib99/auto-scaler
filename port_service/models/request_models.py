from pydantic import BaseModel, Field
from typing import Optional

class CreatePortModel(BaseModel):
    worker_id: int | str
    port_number: int
    port_type: Optional[str] = Field(default=None)

class CreatePortWithWorkerModel(BaseModel):
    port_number: int
    port_type: Optional[str] = Field(default=None)

class UpdatePortModel(BaseModel):
    port_number: Optional[int] = Field(default=None)
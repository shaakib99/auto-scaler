from pydantic import BaseModel, Field
from typing import Optional

class CreatePortModel(BaseModel):
    port_number: int
    port_type: Optional[str] = Field(default=None)

class UpdatePortModel(BaseModel):
    pass
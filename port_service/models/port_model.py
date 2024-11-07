from pydantic import BaseModel, Field
from typing import Optional

class PortModel(BaseModel):
    id: Optional[int] = Field(default=None)
    port_number: Optional[int] = Field(default=None)
    port_type: Optional[str] = Field(default=None)
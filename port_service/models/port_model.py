from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class PortModel(BaseModel):
    id: Optional[int] = Field(default=None)
    port_number: Optional[int] = Field(default=None)
    mapped_port: Optional[int] = Field(default=None)
    port_type: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=True)

    model_config = ConfigDict(
        from_attributes = True,
    )
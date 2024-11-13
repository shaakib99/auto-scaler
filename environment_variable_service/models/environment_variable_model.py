from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class EnvironmentVariableModel(BaseModel):
    worker_id: Optional[int | str] = Field(default=None)
    key: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=True)

    model_config = ConfigDict(
        from_attributes = True,
    )
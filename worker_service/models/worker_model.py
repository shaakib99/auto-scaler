from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from common.enums import WorkerStatusEnum

class WorkerModel(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    container_id: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=WorkerStatusEnum.INIT)
    cpu: Optional[int] = Field(default=1, description="Number cpu core")
    ram: Optional[int] = Field(default=512, description="size of ram in mb")
    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    model_config = ConfigDict(
        from_attributes = True
    )

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from common.enums import WorkerStatusEnum

class WorkerModel(BaseModel):
    id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    status: Optional[str] = Field(default=WorkerStatusEnum.INIT)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())

from typing import Optional
from pydantic import BaseModel, Field
from port_service.models import CreatePortModel

class CreateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
    ports: Optional[list[CreatePortModel]] = Field(default=[])
    environment_variables: Optional[str] = None

class UpdateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
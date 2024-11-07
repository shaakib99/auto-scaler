from typing import Optional
from pydantic import BaseModel, Field
from port_service.models import CreatePortModel
from environment_variable_service.models import CreateEnvironmentVariableModel

class CreateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
    ports: Optional[list[CreatePortModel]] = Field(default=[])
    environment_variables: Optional[CreateEnvironmentVariableModel] = Field(default=[])

class UpdateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
from typing import Optional
from pydantic import BaseModel, Field
from port_service.models import CreatePortWithWorkerModel
from environment_variable_service.models import CreateEnvironmentVariableWithWorkerModel

class CreateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
    ports: Optional[list[CreatePortWithWorkerModel]] = Field(default=[])
    parent_id: Optional[int] = Field(default=None)
    is_cloned: Optional[bool] = Field(default=False)
    environment_variables: Optional[list[CreateEnvironmentVariableWithWorkerModel]] = Field(default=[])

class UpdateWorkerModel(BaseModel):
    ram: Optional[int] = Field(default= 512, description="ram in mb")
    cpu: Optional[int] = Field(default= 1, description="number of cores of cpu")
from pydantic import BaseModel, Field
from typing import Optional
from port_service.models import PortModel
from environment_variable_service.models import EnvironmentVariableModel

class CreateDockerContainerModel(BaseModel):
    container_name: str
    cpu: Optional[int] = Field(default=1, description="number of cpu core")
    ram: Optional[int] = Field(default=512, description="ram in mb")
    exposed_ports: list[PortModel] = Field(default=[])
    environment_variables: list[EnvironmentVariableModel] = Field(default=[])

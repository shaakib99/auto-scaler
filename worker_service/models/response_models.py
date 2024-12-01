from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from port_service.models import PortModel
from environment_variable_service.models import EnvironmentVariableModel

class WorkerResponseModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    status: Optional[str]
    ram: Optional[int]
    cpu: Optional[int]
    parent_id: Optional[int]
    is_cloned: Optional[bool]
    is_active: Optional[bool]
    created_at: Optional[datetime]
    update_at: Optional[datetime]
    ports: Optional[list[PortModel]]
    environment_variables: Optional[list[EnvironmentVariableModel]]
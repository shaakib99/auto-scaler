from pydantic import BaseModel
from typing import Optional

class PortResponseModel(BaseModel):
    id: Optional[int]
    port_number: Optional[int]
    port_type: Optional[str]
from pydantic import BaseModel
from typing import Optional

class ModelMock(BaseModel):
    id: Optional[int]
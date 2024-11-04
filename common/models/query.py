from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    limit: int = 10
    skip: int = 0
    selected_fields: Optional[list[str]]
    join: Optional[list[str]]
    order_by: Optional[str]
    group_by: Optional[str] 
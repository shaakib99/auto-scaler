from pydantic import BaseModel
from datetime import datetime

class TokenBucketParamModel(BaseModel):
    available_tokens: int
    last_updated_time: datetime
from pydantic import BaseModel

class Query(BaseModel):
    limit: int = 10
    skip: int = 0
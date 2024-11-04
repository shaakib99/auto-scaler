from common.abcs import ServiceABC
from database_service.abcs import DatabaseServiceABC
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import TypeVar, Generic

T = TypeVar("T")

class DatabaseService(ServiceABC, Generic[T]):
    def __init__(self, schema: DeclarativeMeta, database:DatabaseServiceABC):
        self. schema = schema
        self.database = database
    
    async def create_one(self, data) -> T:
        pass

    async def update_one(self, id, data) -> T:
        pass

    async def get_one(self, id) -> T:
        pass

    async def get_all(self, query) -> list[T]:
        pass

    async def delete_one(self, id) -> None:
        pass


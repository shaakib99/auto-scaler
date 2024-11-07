from common.abcs import ServiceABC
from database_service.abcs import DatabaseServiceABC
from sqlalchemy.orm import DeclarativeBase
from typing import TypeVar, Generic
from database_service.mysql_service import MySQLDatabaseService
from pydantic import BaseModel

T = TypeVar("T")

class DatabaseService(ServiceABC, Generic[T]):
    def __init__(self, schema: DeclarativeBase, database:DatabaseServiceABC = MySQLDatabaseService()):
        self. schema = schema
        self.database = database
    
    async def create_one(self, data: BaseModel) -> T:
        await self.database.create_one(data, self.schema)

    async def update_one(self, id, data) -> T:
        pass

    async def get_one(self, id) -> T:
        pass

    async def get_all(self, query) -> list[T]:
        pass

    async def delete_one(self, id) -> None:
        pass


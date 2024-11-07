from common.abcs import ServiceABC
from database_service.abcs import DatabaseServiceABC
from sqlalchemy.orm import DeclarativeBase
from typing import TypeVar, Generic
from database_service.mysql_service import MySQLDatabaseService
from common.models import Query
from pydantic import BaseModel

T = TypeVar("T")

class DatabaseService(ServiceABC, Generic[T]):
    def __init__(self, schema: DeclarativeBase, database:DatabaseServiceABC = MySQLDatabaseService()):
        self. schema = schema
        self.database = database
    
    async def create_one(self, data: BaseModel) -> T:
        return await self.database.create_one(data, self.schema)

    async def update_one(self, id, data: BaseModel) -> T:
        return await self.database.update_one(id, data, self.schema)

    async def get_one(self, id: int | str) -> T:
        return await self.database.get_one(id, self.schema)

    async def get_all(self, query: Query) -> list[T]:
        return await self.database.get_all(query, self.schema)

    async def delete_one(self, id) -> None:
        return await self.database.delete_one(id, self.schema)


from abc import ABC, abstractmethod
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
from common.models import Query
from database_service.abcs import DatabaseABC
from typing import TypeVar, Generic

T = TypeVar("T")
class DatabaseServiceABC(ABC, Generic[T]):
    def __init__(self, schema: DeclarativeBase, database_service:DatabaseABC):
        pass

    @staticmethod
    async def connect():
        pass

    @staticmethod
    async def disconnect():
        pass

    @abstractmethod
    async def create_one(self, data: BaseModel, schema: DeclarativeBase) -> T:
        pass

    @abstractmethod
    async def update_one(self, id: str | int, data: BaseModel, schema: DeclarativeBase) -> T:
        pass

    @abstractmethod
    async def get_one(self, id: str | int, schema: DeclarativeBase) -> T:
        pass

    @abstractmethod
    async def get_all(self, query: Query, schema: DeclarativeBase) -> list[T]:
        pass

    @abstractmethod
    async def delete_one(self, id: str | int, schema: DeclarativeBase) -> None:
        pass
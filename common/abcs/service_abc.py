from abc import ABC, abstractmethod
from pydantic import BaseModel
from common.models import Query
from typing import TypeVar, Generic

T = TypeVar("T")

class ServiceABC(ABC, Generic[T]):

    @abstractmethod
    async def create_one(self, data: BaseModel) -> T:
        pass

    @abstractmethod
    async def update_one(self, id: str | int, data: BaseModel) -> T:
        pass

    @abstractmethod
    async def get_one(self, id: str | int) -> T:
        pass

    @abstractmethod
    async def get_all(self, query: Query) -> list[T]:
        pass

    @abstractmethod
    async def delete_one(self, id: str | int) -> None:
        pass
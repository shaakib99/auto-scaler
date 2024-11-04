from abc import ABC, abstractmethod
from pydantic import BaseModel
from common.models import Query

class ServiceABC(ABC):

    @abstractmethod
    async def create_one(self, data: BaseModel):
        pass

    @abstractmethod
    async def update_one(self, id: str | int, data: BaseModel):
        pass

    @abstractmethod
    async def get_one(self, id: str | int):
        pass

    @abstractmethod
    async def get_all(self, query: Query):
        pass

    @abstractmethod
    async def delete_one(self, id: str | int):
        pass
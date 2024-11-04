from abc import ABC, abstractmethod
from pydantic import BaseModel
from sqlalchemy.ext.declarative import DeclarativeMeta
from common.models import Query

class DatabaseServiceABC(ABC):

    @staticmethod
    def get_instance():
        pass

    @staticmethod
    async def connect():
        pass

    @staticmethod
    async def disconnect():
        pass

    @abstractmethod
    async def create_one(self, data: BaseModel, schema: DeclarativeMeta):
        pass

    @abstractmethod
    async def update_one(self, id: str | int, data: BaseModel, schema: DeclarativeMeta):
        pass

    @abstractmethod
    async def get_one(self, id: str | int, schema: DeclarativeMeta):
        pass

    @abstractmethod
    async def get_all(self, query: Query, schema: DeclarativeMeta):
        pass

    @abstractmethod
    async def delete_one(self, id: str | int, schema: DeclarativeMeta):
        pass
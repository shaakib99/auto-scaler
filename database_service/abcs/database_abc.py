from abc import ABC, abstractmethod
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase
from common.models import Query

class DatabaseABC(ABC):

    @staticmethod
    def get_instance():
        pass

    @staticmethod
    def get_base():
        pass

    @staticmethod
    async def connect():
        pass

    @staticmethod
    async def disconnect():
        pass

    @abstractmethod
    async def create_one(self, data: BaseModel, schema: DeclarativeBase):
        pass

    @abstractmethod
    async def update_one(self, id: str | int, data: BaseModel, schema: DeclarativeBase):
        pass

    @abstractmethod
    async def get_one(self, id: str | int, schema: DeclarativeBase):
        pass

    @abstractmethod
    async def get_all(self, query: Query, schema: DeclarativeBase):
        pass

    @abstractmethod
    async def delete_one(self, id: str | int, schema: DeclarativeBase):
        pass
from abc import ABC, abstractmethod


class CacheABC(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    async def get(self, key: str):
        pass

    @abstractmethod
    async def set(self, key: str, value: str, expire: int):
        pass

    @abstractmethod
    async def delete(self, key: str):
        pass
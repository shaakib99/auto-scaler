from cache_service.redis_cache import RedisCache
from cache_service.abcs.cache_abc import CacheABC

class CacheService:
    def __init__(self, cache: CacheABC = None):
        self.cache_service = cache or RedisCache.get_instance()
    
    async def get(self, key: str):
        return await self.cache_service.get(key)
    
    async def set(self, key: str, value: dict, expire = None):
        return await self.cache_service.set(key, value, expire=expire)

    async def delete(self, key: str):
        return await self.cache_service.delete(key)
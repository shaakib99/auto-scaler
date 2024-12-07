from redis import Redis
from cache_service.abcs.cache_abc import CacheABC
import os

class RedisCache(CacheABC):
    instance = None
    def __init__(self):
        self.redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379))
    
    @staticmethod
    def get_instance():
        if RedisCache.instance is None:
            RedisCache.instance = RedisCache()
        return RedisCache.instance
    
    async def connect(self):
        self.redis.ping()
    
    async def disconnect(self):
        self.redis.close()

    async def get(self, key: str):
        return self.redis.get(key)

    async def set(self, key: str, value: dict, expire=None):
        self.redis.set(key, value.__str__())
    
    async def delete(self, key):
        return self.redis.delete(key)
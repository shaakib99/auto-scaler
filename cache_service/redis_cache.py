from redis import Redis
from cache_service.abcs.cache_abc import CacheABC
import os

class RedisCache(CacheABC):
    def __init__(self):
        self.redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), db=os.getenv('REDIS_DB', 'cache_db'))

    async def get(self, key):
        return self.redis.hget(key)

    async def set(self, key, value, expire=None):
        self.redis.hset(key, value)
    
    async def delete(self, key):
        return self.redis.hdel(key)
from functools import wraps
from cache_service.service import CacheService
from database_service.mysql_service import MySQLDatabaseService
from hashlib import md5
from common.abcs import GuardABC
import json

Base = MySQLDatabaseService.get_base() 

def cache(key: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_service = CacheService()
            new_key = md5(key.format(*args, **kwargs).encode('utf-8')).hexdigest()
            result: bytes = await cache_service.get(new_key)
            if result is not None: 
                return json.loads(result.decode('utf-8'))
            
            result = await func(*args, **kwargs)
            if isinstance(result, Base):
                result_dict = {k: v for k, v in result.__dict__.items() if not k.startswith('_')}
                await cache_service.set(new_key, json.dumps(result_dict, default=str))
            else:
                await cache_service.set(new_key, json.dumps(result_dict, default=str))

            return result
        return wrapper
    return decorator


def UseGuard(guard: GuardABC):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            await guard(*args, **kwargs)
            return await func(*args, **kwargs)
        return wrapper
    return decorator
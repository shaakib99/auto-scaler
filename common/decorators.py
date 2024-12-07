from functools import wraps
from cache_service.service import CacheService
from pydantic import BaseModel

def cache(key: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_service = CacheService()
            result = await cache_service.get(key)
            if result is not None: 
                return result
            
            result = await func(*args, **kwargs)

            if isinstance(result, BaseModel):
                await cache_service.set(key, result.model_dump().__str__())
            else:
                await cache_service.set(key, str(result))

            return result
        return wrapper
    return decorator


def UseGuard(guard):
    async def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            await guard(*args, **kwargs)
            return await func(*args, **kwargs)
        return wrapper
    return decorator
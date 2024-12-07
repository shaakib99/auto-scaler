from cache_service.service import CacheService
from pydantic import BaseModel

def cache(key: str):
    """
    A decorator function for caching the result of an asynchronous function.
    
    Parameters:
        key (str): The key to store and retrieve the cached result.

    Returns:
        function: A wrapper function that checks the cache for existing results 
                  and updates the cache with new results.
    """
    cache_service = CacheService()
    def decorator(func):
        async def wrapper(*args, **kwargs):
            result = cache_service.get(key)
            if result is not None: 
                return result
            
            result = await func(*args, **kwargs)

            if isinstance(result, BaseModel):
                cache_service.set(key, result.model_dump().__str__())
            else:
                cache_service.set(key, str(result))

            return result
        return wrapper
    return decorator
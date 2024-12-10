from cache_service.__test__.mocks import *
from unittest.mock import AsyncMock, patch
import pytest

@pytest.fixture
@patch("cache_service.redis_cache.RedisCache")
def redis_instance(redis_cache):
    hmap = {}
    instance = redis_cache()
    instance.get = AsyncMock(side_effect = lambda key: hmap[key] if key in hmap else None)
    instance.set = AsyncMock(side_effect = lambda key, value, expire: hmap.__setitem__(key, value))
    instance.delete = AsyncMock(side_effect = lambda key: hmap.__delitem__(key))
    return instance

import pytest
from cache_service.__test__.mocks import *
from cache_service.service import CacheService

@pytest.fixture
def mock_cache_service(redis_instance):
    service = CacheService(cache = redis_instance)
    return service
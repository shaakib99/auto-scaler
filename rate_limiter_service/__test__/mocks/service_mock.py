import pytest
from cache_service.__test__.mocks import *
from rate_limiter_service.service import RateLimiterService

@pytest.fixture
def mock_rate_limiter_service(mock_cache_service):
    service = RateLimiterService(cache_service=mock_cache_service)
    return service
import pytest
from cache_service.__test__.mocks import *

@pytest.mark.asyncio
async def test_get(mock_cache_service):
    await mock_cache_service.set('test', {'name': 'test'})
    assert await mock_cache_service.get('test') is not None, 'Should return saved data'

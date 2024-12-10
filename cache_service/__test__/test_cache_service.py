import pytest
from cache_service.__test__.mocks import *

@pytest.mark.asyncio
async def test_cache_service(mock_cache_service):
    await mock_cache_service.set('test', {'name': 'test'})
    assert await mock_cache_service.get('test') is not None, 'Should return saved data'

    assert await mock_cache_service.get('test1') is None, 'Should not return saved data'

    await mock_cache_service.delete('test')
    assert await mock_cache_service.get('test') is None, 'Should delete saved data'
import pytest
from worker_discovery_service.__test__.mocks import *

@pytest.mark.asyncio
async def test_get_all(mock_worker_discovery_service):
    result = await mock_worker_discovery_service.get_all()
    assert len(result) > 0, "Should get atleast 1 worker"

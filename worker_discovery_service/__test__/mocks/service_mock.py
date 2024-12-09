import pytest
from worker_discovery_service.service import WorkerDiscoveryService
from worker_service.__test__.mocks import *

@pytest.fixture
def mock_worker_discovery_service(mock_worker_service):
    worker_discovery_service = WorkerDiscoveryService(worker_service=mock_worker_service)
    return worker_discovery_service
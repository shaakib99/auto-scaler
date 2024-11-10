import pytest
from worker_service.models import CreateWorkerModel

@pytest.fixture
def mock_create_worker_model():
    create_worker_model = CreateWorkerModel()
    create_worker_model.cpu = 1
    create_worker_model.ram = 512
    create_worker_model.environment_variables = []
    create_worker_model.ports = []
    return create_worker_model
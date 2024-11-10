import pytest
from worker_service.models import CreateWorkerModel

@pytest.fixture
def mock_create_worker_model():
    create_worker_model = CreateWorkerModel(
        cpu = 1,
        ram = 512,
        environment_variables = [],
        ports = []
    )
    return create_worker_model
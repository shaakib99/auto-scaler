import pytest
from worker_service.models import CreateWorkerModel, UpdateWorkerModel

@pytest.fixture
def mock_create_worker_model():
    create_worker_model = CreateWorkerModel(
        cpu = 1,
        ram = 512,
        environment_variables = [],
        ports = []
    )
    return create_worker_model

@pytest.fixture
def mock_update_worker_model():
    update_worker_model = UpdateWorkerModel(
        cpu=2,
        ram=1024
    )
    return update_worker_model
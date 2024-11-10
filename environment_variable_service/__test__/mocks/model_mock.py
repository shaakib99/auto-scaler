import pytest
from environment_variable_service.models import CreateEnvironmentVariableModel, EnvironmentVariableModel

@pytest.fixture
def mock_create_environment_variable_model():
    create_environment_model = CreateEnvironmentVariableModel()
    create_environment_model.key = "TEST"
    create_environment_model.value = "TEST"
    return create_environment_model

@pytest.fixture
def mock_environment_variable_model():
    environment_model = EnvironmentVariableModel()
    environment_model.key = "TEST"
    environment_model.value = "TEST"
    environment_model.is_active = True
    environment_model.worker_id = 1
    return environment_model
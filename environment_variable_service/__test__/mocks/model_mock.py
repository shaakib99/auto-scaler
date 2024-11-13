import pytest
from environment_variable_service.models import CreateEnvironmentVariableModel, EnvironmentVariableModel, UpdateEnvironmentVariableModel

@pytest.fixture
def mock_create_environment_variable_model():
    create_environment_model = CreateEnvironmentVariableModel(
        key = "TEST",
        value = "TEST",
        worker_id = 1
    )
    return create_environment_model

@pytest.fixture
def mock_update_environment_variable_model():
    update_environment_model = UpdateEnvironmentVariableModel(
        key = "TEST",
        value = "TEST",
    )
    return update_environment_model

@pytest.fixture
def mock_environment_variable_model():
    environment_model = EnvironmentVariableModel()
    environment_model.key = "TEST"
    environment_model.value = "TEST"
    environment_model.is_active = True
    environment_model.worker_id = 1
    return environment_model
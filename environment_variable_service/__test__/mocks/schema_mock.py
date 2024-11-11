import pytest
from environment_variable_service.schema import EnvironmentVariableSchema

@pytest.fixture
def mock_environment_variable_schema():
    environment_variable_schema = EnvironmentVariableSchema()
    environment_variable_schema.id = 1
    environment_variable_schema.worker_id = 1
    environment_variable_schema.key = "TEST"
    environment_variable_schema.value = "TEST"
    return environment_variable_schema
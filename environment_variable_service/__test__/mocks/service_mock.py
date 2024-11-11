import pytest
from environment_variable_service.service import EnvironmentVariableService
from database_service.__test__.mocks import mock_database_service

@pytest.fixture
def mock_environment_variable_service(mock_database_service):
    service = EnvironmentVariableService(environment_variable_model=mock_database_service)
    return service

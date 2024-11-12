import pytest
from unittest.mock import AsyncMock
from environment_variable_service.service import EnvironmentVariableService
from database_service.__test__.mocks import *
from environment_variable_service.__test__.mocks.model_mock import *

@pytest.fixture
def mock_environment_variable_service(mock_database_service, mock_environment_variable_schema):
    mock_database_service.create_one = AsyncMock(return_value = mock_environment_variable_schema)
    mock_database_service.update_one = AsyncMock(side_effect = lambda id, data: mock_environment_variable_schema if id == 1 else None)
    mock_database_service.get_one = AsyncMock(side_effect = lambda id, data: mock_environment_variable_schema if id == 1 else None)
    mock_database_service.get_all = AsyncMock(return_value = [mock_environment_variable_schema])
    service = EnvironmentVariableService(environment_variable_model=mock_database_service)
    return service

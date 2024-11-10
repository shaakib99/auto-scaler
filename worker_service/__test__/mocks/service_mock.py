from worker_service.service import WorkerService
from database_service.__test__.mocks import mock_database_service
from port_service.__test__.mocks import mock_port_schema
from unittest.mock import AsyncMock
import pytest

@pytest.fixture
def mock_worker_service(mock_database_service, mock_docker_service, mock_port_service, mock_environment_variable_service):
    mock_port_service.create_one = AsyncMock(return_value = mock_port_schema)
    
    service = WorkerService(
        worker_model=mock_database_service,
        docker_service=mock_docker_service,
        port_service=mock_port_service,
        environment_variable_service=mock_environment_variable_service
    )
    return service
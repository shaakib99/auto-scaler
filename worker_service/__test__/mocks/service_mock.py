from worker_service.service import WorkerService
from database_service.__test__.mocks import *
from docker_service.__test__.mocks import *
from unittest.mock import AsyncMock
import pytest

@pytest.fixture
def mock_worker_service(
    mock_database_service, 
    mock_docker_service, 
    mock_port_service, 
    mock_environment_variable_service,
    mock_worker_schema,
    ):
    mock_database_service.create_one = AsyncMock(return_value = mock_worker_schema)
    mock_database_service.update_one = AsyncMock(side_effect = lambda id, data: mock_worker_schema if id == 1 else None)
    mock_database_service.get_one = AsyncMock(side_effect = lambda id = mock_worker_schema.id: mock_worker_schema if id == 1 else None)
    mock_database_service.get_all = AsyncMock(return_value = [mock_worker_schema])

    service = WorkerService(
        worker_model=mock_database_service,
        docker_service=mock_docker_service,
        port_service=mock_port_service,
        environment_variable_service=mock_environment_variable_service
    )
    return service
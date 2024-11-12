import pytest
from unittest.mock import AsyncMock
from port_service.service import PortService
from database_service.__test__.mocks import *
from port_service.__test__.mocks.model_mock import *

@pytest.fixture
def mock_port_service(mock_database_service, mock_port_schema):
    mock_database_service.create_one = AsyncMock(return_value = mock_port_schema)
    mock_database_service.update_one = AsyncMock(side_effect = lambda id, data: mock_port_schema if id == 1 else None)
    mock_database_service.get_one = AsyncMock(side_effect = lambda id, data: mock_port_schema if id == 1 else None)
    mock_database_service.get_all = AsyncMock(return_value = [mock_port_schema])

    service = PortService(port_model=mock_database_service)
    return service


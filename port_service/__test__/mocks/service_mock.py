import pytest
from unittest.mock import AsyncMock
from port_service.service import PortService
from database_service.__test__.mocks import *
from port_service.__test__.mocks.model_mock import *

@pytest.fixture
def mock_port_service(mock_database_service, mock_port_schema):
    service = PortService(port_model=mock_database_service)
    service.create_one = AsyncMock(return_value = mock_port_schema)
    return service


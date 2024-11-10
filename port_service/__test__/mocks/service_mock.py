import pytest
from port_service.service import PortService
from database_service.__test__.mocks import mock_database_service

@pytest.fixture
def mock_port_service(mock_database_service):
    service = PortService(port_model=mock_database_service)
    return service


import pytest
from port_service.models import CreatePortModel, PortModel

@pytest.fixture
def mock_create_port_model():
    create_port_model = CreatePortModel()
    create_port_model.port_number = 10001
    create_port_model.port_type = "TEST"
    return create_port_model

@pytest.fixture
def mock_port_model():
    port_model = PortModel()
    port_model.id = 1
    port_model.port_number = 10001
    port_model.port_type = "TEST"
    port_model.mapped_port = 10002
    port_model.is_active = True
    return port_model


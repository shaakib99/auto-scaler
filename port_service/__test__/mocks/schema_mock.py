import pytest
from port_service.schema import PortSchema
from datetime import datetime

@pytest.fixture
def mock_port_schema():
    port_schema = PortSchema()
    port_schema.id = 1
    port_schema.worker_id = 1
    port_schema.port_number = 10001
    port_schema.mapped_port = 10002
    port_schema.port_type = "TEST"
    port_schema.is_active = True
    port_schema.created_at = datetime.now()
    port_schema.updated_at = datetime.now()
    return port_schema
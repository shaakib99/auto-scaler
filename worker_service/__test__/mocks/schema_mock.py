import pytest
from worker_service.schema import WorkerSchema
from common.enums import WorkerStatusEnum
from datetime import datetime

@pytest.fixture
def mock_worker_schema():
    worker_schema = WorkerSchema()
    worker_schema.id = 1
    worker_schema.container_id = "12345"
    worker_schema.name = "TEST"
    worker_schema.cpu = 1
    worker_schema.ram = 512
    worker_schema.status = WorkerStatusEnum.INIT
    worker_schema.is_active = True
    worker_schema.created_at = datetime.now()
    worker_schema.updated_at = datetime.now()
    return worker_schema
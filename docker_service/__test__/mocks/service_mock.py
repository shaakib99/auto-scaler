import pytest
from unittest.mock import AsyncMock
from docker_service.service import DockerContainerService

@pytest.fixture
def mock_docker_service():
    service = DockerContainerService()
    service.create_one = AsyncMock(return_value = "TEST")
    return service
import pytest
from unittest.mock import AsyncMock, MagicMock
from docker_service.service import DockerContainerService, docker

@pytest.fixture
def mock_docker_service():
    docker.from_env = MagicMock()
    service = DockerContainerService()
    service.create_one = AsyncMock(return_value = "TEST")
    return service
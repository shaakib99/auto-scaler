import pytest
from docker_service.service import DockerContainerService

@pytest
def mock_docker_service():
    service = DockerContainerService()
    return service
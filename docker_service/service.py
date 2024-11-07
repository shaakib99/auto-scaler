from docker_service.models import CreateDockerContainerModel

class DockerContainerService:
    def __init__(self):
        pass

    async def create_one(self, data: CreateDockerContainerModel):
        pass

    async def stop_one(self, name: str):
        pass

    async def remove_one(self, name: str):
        pass
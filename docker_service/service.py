from docker_service.models import CreateDockerContainerModel
import docker

class DockerContainerService:
    def __init__(self):
        pass

    async def create_one(self, data: CreateDockerContainerModel) -> str:
        client = docker.from_env()
        image = client.images.pull(data.image_name)
        container = client.containers.run(
            image.id, 
            name = data.container_name,
            detach = True,
            ports = data.exposed_ports,
            environment = data.environment_variables
        )
        return container.id

    async def stop_one(self, id: str):
        client = docker.from_env()
        container = client.containers.get(id)
        container.stop()
        return container.id

    async def remove_one(self, name: str):
        client = docker.from_env()
        container = client.containers.get(id)
        container.remove()
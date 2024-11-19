from docker_service.models import CreateDockerContainerModel
import docker

class DockerContainerService:
    def __init__(self):
        self.client = docker.from_env()

    async def create_one(self, data: CreateDockerContainerModel) -> str:
        image = self.client.images.pull(data.image_name)

        exposed_ports = []
        env_variables = []
        for port in data.exposed_ports:
            exposed_ports.append({port.port_number: port.mapped_port})
        
        for env_variable in data.environment_variables:
            env_variables.append(f"{env_variable.key}={env_variable.value}")
        
        
        container = self.client.containers.run(
            image.id, 
            name = data.container_name,
            detach = True,
            ports = exposed_ports,
            environment = env_variables
        )
        return container.id

    async def stop_one(self, id: str):
        container = self.client.containers.get(id)
        container.stop()
        return container.id

    async def remove_one(self, name: str):
        container = self.client.containers.get(id)
        container.remove()
    
    async def get_stats(self, id: str):
        container = self.client.containers.get(id)
        return container.stats(stream=False)
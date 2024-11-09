from common.abcs import ServiceABC
from common.models import Query
from common.enums import WorkerStatusEnum
from common.exceptions import NotFoundException
from worker_service.schema import WorkerSchema
from worker_service.models import CreateWorkerModel, UpdateWorkerModel, WorkerModel
from port_service.models import CreatePortModel, PortModel
from port_service.schema import PortSchema
from port_service.service import PortService
from environment_variable_service.models import CreateEnvironmentVariableModel, EnvironmentVariableModel
from environment_variable_service.schema import EnvironmentVariableSchema
from environment_variable_service.service import EnvironmentVariableService
from database_service.service import DatabaseService
from docker_service.service import DockerContainerService
from docker_service.models import CreateDockerContainerModel
import uuid

class WorkerService(ServiceABC):
    def __init__(self, 
        worker_model = DatabaseService[WorkerSchema](WorkerSchema),
        docker_service = DockerContainerService(),
        port_service = PortService(),
        environment_variable_service = EnvironmentVariableService()
        ):
        self.worker_model = worker_model
        self.port_service = port_service
        self.environment_variable_service = environment_variable_service
        self.docker_service = docker_service
    
    async def get_one(self, id: int | str):
        data = await self.worker_model.get_one(id)
        if not data:
            raise NotFoundException(f"{id} not found")
        return data
    
    async def get_all(self, query: Query):
        return await self.worker_model.get_all(query)
    
    async def create_one(self, data: CreateWorkerModel):
        worker = WorkerModel()
        worker.cpu = data.cpu
        worker.ram = data.ram
        worker.name = f"worker-{uuid.uuid4().__str__()}"
        worker.status = WorkerStatusEnum.INIT

        worker_data = await self.worker_model.create_one(worker)

        # run docker container
        create_docker_container_data = CreateDockerContainerModel()
        create_docker_container_data.image_name = "dockerhub.io/worker"
        create_docker_container_data.container_name = worker.name
        create_docker_container_data.cpu = worker.cpu
        create_docker_container_data.ram = worker.ram

        exposed_ports: list[PortSchema] = []
        for item in data.ports:
            port = CreatePortModel()
            port.worker_id = item.worker_id
            port.port_number = item.port_number
            port.port_type = item.port_type
            port_data = await self.port_service.create_one(port)
            exposed_ports.append(PortModel.model_validate(port_data))
        
        environment_variables: list[EnvironmentVariableSchema] = []
        for item in data.environment_variables:
            environment_variable = CreateEnvironmentVariableModel()
            environment_variable.worker_id = item.worker_id
            environment_variable.key = item.key
            environment_variable.value = item.value
            environment_variable_data = await self.environment_variable_service.create_one(environment_variable)
            environment_variables.append(EnvironmentVariableModel.model_validate(environment_variable_data))
            

        create_docker_container_data.exposed_ports = exposed_ports
        create_docker_container_data.environment_variables = environment_variables
        container_id = await self.docker_service.create_one(create_docker_container_data)

        worker.container_id = container_id
        del worker.status
        worker_data = self.update_one(worker_data.id, worker)
        return worker_data

    
    async def update_one(self, id: int | str, data: UpdateWorkerModel):
        existing_data = await self.get_one(id)
        return await self.worker_model.update_one(id, data)
    
    async def delete_one(self, id: str | int):
        existing_data = await self.get_one(id)
        return await self.worker_model.delete_one(id)
    

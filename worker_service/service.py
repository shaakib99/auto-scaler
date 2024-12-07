from common.abcs import ServiceABC
from common.models import Query
from common.enums import WorkerStatusEnum
from common.exceptions import NotFoundException, BadRequestException
from worker_service.schema import WorkerSchema
from worker_service.models import CreateWorkerModel, UpdateWorkerModel, WorkerModel
from port_service.models import CreatePortModel, PortModel, CreatePortWithWorkerModel
from port_service.schema import PortSchema
from environment_variable_service.models import CreateEnvironmentVariableModel, EnvironmentVariableModel, CreateEnvironmentVariableWithWorkerModel
from environment_variable_service.schema import EnvironmentVariableSchema
from database_service.service import DatabaseService
from database_service.abcs import DatabaseServiceABC
from docker_service.service import DockerContainerService
from docker_service.models import CreateDockerContainerModel
import uuid

class WorkerService(ServiceABC):
    def __init__(self, 
        worker_model: DatabaseServiceABC[WorkerSchema] = None,
        docker_service: DockerContainerService = None,
        port_service: ServiceABC[PortSchema] = None,
        environment_variable_service: ServiceABC[EnvironmentVariableSchema] = None
        ):
        self.worker_model = worker_model or DatabaseService(WorkerSchema)
        self._port_service = port_service
        self._environment_variable_service = environment_variable_service
        self.docker_service = docker_service or DockerContainerService()
    
    @property
    def port_service(self):
        if self._port_service is None:
            from port_service.service import PortService
            self._port_service = PortService()
        return self._port_service
    
    @property
    def environ_variable_service(self):
        if self._environment_variable_service is None:
            from environment_variable_service.service import EnvironmentVariableService
            self._environment_variable_service = EnvironmentVariableService()
        return self._environment_variable_service
    
    async def get_one(self, id: int | str):
        data = await self.worker_model.get_one(id)
        if not data:
            raise NotFoundException(f"{id=} not found")
        return data
    
    async def get_all(self, query: Query):
        return await self.worker_model.get_all(query)
    
    async def create_one(self, data: CreateWorkerModel):
        worker = WorkerModel()
        worker.cpu = data.cpu
        worker.ram = data.ram
        worker.name = f"worker-{uuid.uuid4().__str__()}"
        worker.status = WorkerStatusEnum.INIT.value

        worker_data = await self.worker_model.create_one(worker)

        # run docker container
        create_docker_container_data = CreateDockerContainerModel(
            image_name = "shaakib99/cache-fastapi2:latest",
            container_name = worker.name
        )
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
        worker.status = WorkerStatusEnum.RUNNING.value
        worker_data = await self.worker_model.update_one(worker_data.id, worker)
        return worker_data

    
    async def update_one(self, id: int | str, data: UpdateWorkerModel):
        worker = await self.get_one(id)
        worker_model = WorkerModel.model_validate(worker)
        for key in data.model_fields_set:
            setattr(worker_model, key, getattr(data, key))
        return await self.worker_model.update_one(id, worker_model)
    
    async def delete_one(self, id: str | int):
        worker = await self.get_one(id)
        if worker.is_cloned is False:
            raise BadRequestException(f'{id} is not a cloned worker')

        await self.docker_service.remove_one(worker.container_id)
        return await self.worker_model.delete_one(id)
    
    async def clone_worker(self, id: str | int):
        worker = await self.get_one(id)
        create_worker_model = CreateWorkerModel(
            cpu = worker.cpu,
            ram = worker.ram,
            parent_id = worker.id,
            is_cloned = True
        )

        ports = await self.port_service.get_all(Query(filter_by=f"worker_id={worker.id}", limit=100000))
        environment_variables = await self.environ_variable_service.get_all(Query(filter_by=f"worker_id={worker.id}", limit=100000))

        for port in ports:
            create_port_model = CreatePortWithWorkerModel(
                port = port.port_number,
                port_type = port.port_type
            )
            create_worker_model.ports.append(create_port_model)
        
        for environment_variable in environment_variables:
            create_environment_variable_model = CreateEnvironmentVariableWithWorkerModel(
                key = environment_variable.key,
                value = environment_variable.value
            )
            create_worker_model.environment_variables.append(create_environment_variable_model)
        
        result = await self.create_one(create_worker_model)
        return result
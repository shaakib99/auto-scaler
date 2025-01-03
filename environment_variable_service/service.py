from common.abcs import ServiceABC
from common.models import Query
from common.exceptions import NotFoundException
from environment_variable_service.models import CreateEnvironmentVariableModel, UpdateEnvironmentVariableModel, EnvironmentVariableModel
from environment_variable_service.schema import EnvironmentVariableSchema
from database_service.service import DatabaseService
from database_service.abcs import DatabaseServiceABC
from worker_service.schema import WorkerSchema   


class EnvironmentVariableService(ServiceABC):
    def __init__(self, 
        environment_variable_model: DatabaseServiceABC[EnvironmentVariableSchema] = None, 
        worker_service: ServiceABC[WorkerSchema] = None):
        self.environment_variable_model = environment_variable_model or DatabaseService(EnvironmentVariableSchema)
        self._worker_service = worker_service
    
    @property
    def worker_service(self):
        if self._worker_service is None:
            from worker_service.service import WorkerService 
            self._worker_service = WorkerService()
        return self._worker_service

    async def create_one(self, data: CreateEnvironmentVariableModel):
        worker = await self.worker_service.get_one(data.worker_id)
        if not worker:
            raise NotFoundException(f"worker id {data.worker_id} not found")
        environment_variable = EnvironmentVariableModel()
        environment_variable.worker_id = data.worker_id
        environment_variable.key = data.key
        environment_variable.value = data.value
        return await self.environment_variable_model.create_one(environment_variable)
    
    async def update_one(self, id: int | str, data: UpdateEnvironmentVariableModel):
        environ_variable = await self.get_one(id)
        environ_variable_model = EnvironmentVariableModel.model_validate(environ_variable)
        for key in data.model_fields_set:
            setattr(environ_variable_model, key, getattr(data, key))
        return await self.environment_variable_model.update_one(id, environ_variable_model)
    
    async def get_one(self, id: int | str):
        return await self.environment_variable_model.get_one(id)
    
    async def get_all(self, query: Query):
        return await self.environment_variable_model.get_all(query)
    
    async def delete_one(self, id: int | str):
        return await self.environment_variable_model.delete_one(id)
        
from common.abcs import ServiceABC
from environment_variable_service.models import CreateEnvironmentVariableModel, UpdateEnvironmentVariableModel, EnvironmentVariableModel
from environment_variable_service.schema import EnvironmentVariableSchema
from database_service.service import DatabaseService
from common.models import Query


class EnvironmentVariableService(ServiceABC):
    def __init__(self, environment_variable_model: DatabaseService[EnvironmentVariableSchema]):
        self.environment_variable_model = environment_variable_model or DatabaseService[EnvironmentVariableSchema](EnvironmentVariableSchema)
    
    async def create_one(self, data: CreateEnvironmentVariableModel):
        environment_variable_model = EnvironmentVariableModel()
        environment_variable_model.worker_id = data.worker_id
        environment_variable_model.key = data.key
        environment_variable_model.value = data.value
        return await self.environment_variable_model.create_one(environment_variable_model)
    
    async def update_one(self, id: int | str, data: UpdateEnvironmentVariableModel):
        environ_variable = await self.get_one(id)
        environ_variable_model = EnvironmentVariableModel.model_validate(environ_variable)
        environ_variable_model.key = data.key
        environ_variable_model.value = data.value
        return await self.environment_variable_model.update_one(id, environ_variable_model)
    
    async def get_one(self, id: int | str):
        return await self.environment_variable_model.get_one(id)
    
    async def get_all(self, query: Query):
        return await self.environment_variable_model.get_all(query)
    
    async def delete_one(self, id: int | str):
        return await self.environment_variable_model.delete_one(id)
        
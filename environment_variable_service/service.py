from common.abcs import ServiceABC
from environment_variable_service.models import CreateEnvironmentVariableModel, UpdateEnvironmentVariableModel
from environment_variable_service.schema import EnvironmentVariableSchema
from database_service.service import DatabaseService
from common.models import Query


class EnvironmentVariableService(ServiceABC):
    def __init__(self, environment_variable_model = DatabaseService[EnvironmentVariableSchema](EnvironmentVariableSchema)):
        self.environment_variable_model = environment_variable_model
    
    async def create_one(self, data: CreateEnvironmentVariableModel):
        return await self.environment_variable_model.create_one(data)
    
    async def update_one(self, id: int | str, data: UpdateEnvironmentVariableModel):
        return await self.environment_variable_model.update_one(id, data)
    
    async def get_one(self, id: int | str):
        return await self.environment_variable_model.get_one(id)
    
    async def get_all(self, query: Query):
        return await self.environment_variable_model.get_all(query)
    
    async def delete_one(self, id: int | str):
        return await self.environment_variable_model.delete_one(id)
        
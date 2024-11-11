from common.abcs import ServiceABC
from common.models import Query
from database_service.service import DatabaseService
from port_service.schema import PortSchema
from port_service.models import CreatePortModel, UpdatePortModel

class PortService(ServiceABC):
    def __init__(self, port_model: DatabaseService[PortSchema]):
        self.port_model = port_model or  DatabaseService[PortSchema](PortSchema)
    
    async def create_one(self, data: CreatePortModel):
        return await self.port_model.create_one(data)
    
    async def update_one(self, id: int | str, data: UpdatePortModel):
        return await self.port_model.update_one(data)
    
    async def get_one(self, id: int | str):
        return await self.port_model.get_one(id)
    
    async def get_all(self, query: Query):
        return await self.get_all(query)
    
    async def delete_one(self, id: int | str):
        return await self.port_model.delete_one(id)
    
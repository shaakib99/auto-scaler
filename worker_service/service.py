from common.abcs import ServiceABC
from common.models import Query
from common.exceptions import NotFoundException
from worker_service.schema import WorkerSchema
from database_service.service import DatabaseService

class WorkerService(ServiceABC):
    def __init__(self, worker_model = DatabaseService[WorkerSchema](WorkerSchema)):
        self.worker_model = worker_model
    
    async def get_one(self, id: int | str):
        data = await self.worker_model.get_one(id)
        if not data:
            raise NotFoundException(f"{id} not found")
        return data
    
    async def get_all(self, query: Query):
        return await self.worker_model.get_all(query)
    
    async def create_one(self, data):
        return await self.worker_model.create_one(data)
    
    async def update_one(self, id: int | str, data):
        existing_data = await self.get_one(id)
        return await self.worker_model.update_one(id, data)
    
    async def delete_one(self, id: str | int):
        existing_data = await self.get_one(id)
        return await self.worker_model.delete_one(id)
    

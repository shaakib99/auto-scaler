from common.abcs import ServiceABC
from common.models import Query
from common.exceptions import NotFoundException
from database_service.service import DatabaseService
from database_service.abcs import DatabaseServiceABC
from port_service.schema import PortSchema
from port_service.models import CreatePortModel, UpdatePortModel, PortModel
from worker_service.schema import WorkerSchema
from worker_service.service import WorkerService
from utils.helper import get_open_port

class PortService(ServiceABC):
    def __init__(self, 
        port_model: DatabaseServiceABC[PortSchema] = None,
        worker_service: ServiceABC[WorkerSchema] = None):
        self.port_model = port_model or  DatabaseService[PortSchema](PortSchema)
        self.worker_service = worker_service or WorkerService()
    
    async def create_one(self, data: CreatePortModel):
        worker = await self.worker_service.get_one(data.worker_id)
        if not worker:
            raise NotFoundException(f"Worker Id {data.worker_id} not found")
        port_model = PortModel()
        port_model.port_number = data.port_number
        port_model.port_type = data.port_type
        port_model.worker_id = data.worker_id
        port_model.mapped_port = get_open_port()
        return await self.port_model.create_one(port_model)
    
    async def update_one(self, id: int | str, data: UpdatePortModel):
        port = await self.get_one(id)
        port_model = PortModel.from_orm(port)
        return await self.port_model.update_one(id, port_model)
    
    async def get_one(self, id: int | str):
        port = await self.port_model.get_one(id)
        if not port:
            raise NotFoundException(f"{id} not found")
        return port
    
    async def get_all(self, query: Query):
        return await self.port_model.get_all(query)
    
    async def delete_one(self, id: int | str):
        port = await self.get_one(id)
        return await self.port_model.delete_one(id)
    
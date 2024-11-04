from common.abcs import ServiceABC
from worker_service.schema import WorkerSchema
from database_service.service import DatabaseService

class WorkerService(ServiceABC):
    def __init__(self, worker_model = DatabaseService[WorkerSchema](WorkerSchema)):
        self.worker_model = worker_model
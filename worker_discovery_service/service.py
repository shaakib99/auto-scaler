from worker_service.service import WorkerService
from worker_discovery_service.models import PrometheusHTTPServiceDiscoveryResponseModel
from common.models import Query

class WrokerDiscoveryService:
    def __init__(self, worker_service: WorkerService = None):
        self.worker_service = worker_service or WorkerService()

    async def get_all(self):
        query = Query()
        query.limit = 10000
        query.filter_by = "status='running'"
        workers = await self.worker_service.get_all(query)

        prometheus_response_model = PrometheusHTTPServiceDiscoveryResponseModel()
        
        for worker in workers:
            host = 'host.docker.internal:8000'
            metrics_path = f'{worker.container_id}/metrics'
            prometheus_response_model.targets.append(host)
            prometheus_response_model.labels['__metrics_path__'] = metrics_path
        return [prometheus_response_model]

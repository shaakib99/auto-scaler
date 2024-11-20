from fastapi import APIRouter
from worker_discovery_service.service import WrokerDiscoveryService

router = APIRouter(prefix='/services')

worker_discovery_service = WrokerDiscoveryService()

@router.get('')
async def service_discovery():
    return await worker_discovery_service.get_all()

from fastapi import APIRouter
from metrics_service.service import MetricsService

router = APIRouter(prefix='')

metrics_service = MetricsService()

@router.get('/{container_id}/metrics')
async def get_matrics(container_id: str):
    return await metrics_service.generate_metrics(container_id)
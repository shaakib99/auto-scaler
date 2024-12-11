from fastapi import APIRouter, Depends, Request
from typing import Annotated
from common.models import Query
from worker_service.service import WorkerService
from worker_service.models import CreateWorkerModel, WorkerResponseModel
from common.decorators import cache
from common.enums import CacheKeysEnum
from metrics_service.models import AlertData

router = APIRouter(prefix='/workers')

worker_service = WorkerService()

@router.post('/clone', response_model=WorkerResponseModel)
async def clone_worker(data: AlertData):
    return await worker_service.clone_worker(data.commonAnnotations.instance)

@router.post('/remove', response_model=WorkerResponseModel)
async def remove_worker(data: AlertData):
    return await worker_service.remove_worker(data.commonAnnotations.instance)

@router.get('/{id}', status_code=200, response_model=WorkerResponseModel, response_model_exclude_none=True)
@cache(CacheKeysEnum.WORKER_GET_ONE.value)
async def get_one(id: int | str, request: Request):
    return await worker_service.get_one(id)

@router.get('', status_code=200, response_model=list[WorkerResponseModel], response_model_exclude_none=True)
async def get_all(query : Annotated[Query, Depends(Query)]):
    return await worker_service.get_all(query)

@router.post('', status_code=201, response_model=WorkerResponseModel, response_model_exclude_none=True)
async def create_one(data: CreateWorkerModel):
    return await worker_service.create_one(data)

@router.patch('/{id}', status_code=200, response_model=WorkerResponseModel, response_model_exclude_none=True)
async def update_one(id: int | str, data):
    return await worker_service.update_one(id, data)

@router.delete('/{id}', status_code=200, response_model=None)
async def delete_one(id: int | str):
    return await worker_service.delete_one(id)
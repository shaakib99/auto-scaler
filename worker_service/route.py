from fastapi import APIRouter, Depends
from typing import Annotated
from common.models import Query
from worker_service.service import WorkerService
from worker_service.models import CreateWorkerModel, WorkerModel

router = APIRouter('/workers')

worker_service = WorkerService()

@router.get('/{id}', status_code=200, response_model=WorkerModel, response_model_exclude_none=True)
async def get_one(id: int | str):
    return await worker_service.get_one(id)

@router.get('', status_code=200, response_model=list[WorkerModel], response_model_exclude_none=True)
async def get_all(query : Annotated[Query, Depends(Query)]):
    return await worker_service.get_all(query)

@router.post('', status_code=201, response_model=list[WorkerModel], response_model_exclude_none=True)
async def create_one(data: CreateWorkerModel):
    return await worker_service.create_one(data)

@router.patch('/{id}', status_code=200, response_model=WorkerModel, response_model_exclude_none=True)
async def update_one(id: int | str, data):
    return await worker_service.update_one(id, data)

@router.delete('/{id}', status_code=200, response_model=None)
async def delete_one(id: int | str):
    return await worker_service.delete_one(id)
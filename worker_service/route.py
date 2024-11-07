from fastapi import APIRouter, Depends
from typing import Annotated
from common.models import Query
from worker_service.service import WorkerService

router = APIRouter('/workers')

worker_service = WorkerService()

@router.get('/{id}')
async def get_one(id: int | str):
    return await worker_service.get_one(id)

@router.get('')
async def get_all(query : Annotated[Query, Depends(Query)]):
    return await worker_service.get_all(query)

@router.post('')
async def create_one(data):
    return await worker_service.create_one(data)

@router.patch('/{id}')
async def update_one(id: int | str, data):
    return await worker_service.update_one(id, data)

@router.delete('/{id}')
async def delete_one(id: int | str):
    return await worker_service.delete_one(id)
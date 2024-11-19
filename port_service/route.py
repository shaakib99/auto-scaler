from fastapi import APIRouter, Depends
from port_service.service import PortService
from port_service.models import CreatePortModel, UpdatePortModel, PortResponseModel
from common.models import Query
from typing import Annotated

router = APIRouter(prefix="/ports")

port_service = PortService()

@router.get("/{id}", response_model=PortResponseModel, response_model_exclude_none=True)
async def get_one(id: int | str):
    return await port_service.get_one(id)

@router.get("", response_model=list[PortResponseModel], response_model_exclude_none=True)
async def get_all(query: Annotated[Query, Depends(Query)]):
    return await port_service.get_all(query)

@router.post("", status_code=201, response_model=PortResponseModel, response_model_exclude_none=True)
async def create_one(data: CreatePortModel):
    return await port_service.create_one(data)

@router.patch("/{id}", response_model=PortResponseModel, response_model_exclude_none=True)
async def update_one(id: int | str, data: UpdatePortModel):
    return await port_service.update_one(id, data)

@router.delete("/{id}")
async def delete_one(id: int | str):
    return await port_service.delete_one(id)

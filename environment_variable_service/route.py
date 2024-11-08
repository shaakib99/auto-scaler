from fastapi import APIRouter, Depends
from common.models import Query
from typing import Annotated
from environment_variable_service.models import CreateEnvironmentVariableModel, UpdateEnvironmentVariableModel, ResponseEnvironmentVariableModel
from environment_variable_service.service import EnvironmentVariableService

router = APIRouter("/environment-variables")

environment_variable_service = EnvironmentVariableService()

@router.get("/{id}", response_model=ResponseEnvironmentVariableModel, response_model_exclude_none=True)
async def get_one(id: int | str):
    return await environment_variable_service.get_one(id)

@router.get("", response_model=list[ResponseEnvironmentVariableModel], response_model_exclude_none=True)
async def get_all(query: Annotated[Query, Depends(Query)]):
    return await environment_variable_service.get_all(query)

@router.post("", status_code=201, response_model=ResponseEnvironmentVariableModel, response_model_exclude_none=True)
async def create_one(data: CreateEnvironmentVariableModel):
    return await environment_variable_service.create_one(data)

@router.patch("/{id}", response_model=ResponseEnvironmentVariableModel, response_model_exclude_none=True)
async def update_one(id: int | str, data: UpdateEnvironmentVariableModel):
    return await environment_variable_service.update_one(id, data)

@router.delete("/{id}")
async def delete_one(id: int | str):
    return await environment_variable_service.delete_one(id)
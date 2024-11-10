from unittest.mock import MagicMock
from database_service.__test__.mocks import MockSchema, ModelMock, db_instance
from database_service.mysql_service import MySQLDatabaseService
from common.models import Query
import pytest


@pytest.mark.asyncio
async def test_connect(db_instance):
    MySQLDatabaseService.get_instance = MagicMock(return_value = db_instance)
    await MySQLDatabaseService.connect()

@pytest.mark.asyncio
async def test_disconnect(db_instance):
    db_instance.get_instance =  MagicMock(return_value = db_instance)
    await MySQLDatabaseService.disconnect()

@pytest.mark.asyncio
async def test_create_one(db_instance):
    result = await db_instance.create_one(ModelMock(id = 1), MockSchema)
    assert result.id is not None, "must return result"

@pytest.mark.asyncio
async def test_update_one(db_instance):
    result = await db_instance.update_one(1, ModelMock(id = 1), MockSchema)
    assert result.id == 1, "id should be 1"

    result = await db_instance.update_one(2, ModelMock(id = 1), MockSchema)
    assert result is None, "result should None"

@pytest.mark.asyncio
async def test_get_one(db_instance):
    result = await db_instance.get_one(1, MockSchema)
    assert result.id == 1, "id should be 1"

    result = await db_instance.get_one(2, MockSchema)
    assert result is None, "result should None"

@pytest.mark.asyncio
async def test_get_all(db_instance):
    result = await db_instance.get_all(Query(), MockSchema)
    assert len(result) == 1, "length of the result should be 1"

@pytest.mark.asyncio
async def test_delete_one(db_instance):
    result = await db_instance.delete_one(1, MockSchema)
    assert result is None, "result should None"

    
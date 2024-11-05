import pytest
from unittest.mock import AsyncMock, patch
from .schema_mock import MockSchema


@pytest.fixture
@patch('database_service.mysql_service.MySQLDatabaseService')
def db_instance(db):
    mock_result = MockSchema(id = 1)
    instance = db()
    instance.connect = AsyncMock()
    instance.disconnect = AsyncMock()
    instance.create_one = AsyncMock(return_value = mock_result)
    instance.update_one = AsyncMock(side_effect = lambda id, data, schema: mock_result if id == 1 else None)
    instance.delete_one = AsyncMock(return_value = None)
    instance.get_one = AsyncMock(side_effect = lambda id, schema: mock_result if id == 1 else None)
    instance.get_all = AsyncMock(return_value = [mock_result])


    return instance

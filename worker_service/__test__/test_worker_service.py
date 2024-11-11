from worker_service.__test__.mocks import *
from database_service.__test__.mocks import *
from docker_service.__test__.mocks import *
from port_service.__test__.mocks import *
from environment_variable_service.__test__.mocks import *
import pytest

@pytest.mark.asyncio
async def test_create_one(
    mock_worker_service,
    mock_create_worker_model
    ):
    result = await mock_worker_service.create_one(mock_create_worker_model)
    assert result.id is not None, "create worker method must return insert id"
    assert result.name is not None, "create worker method must return insert name"

@pytest.mark.asyncio
async def test_update_one(
    mock_worker_service,
    mock_update_worker_model
    ):
    result = await mock_worker_service.update_one(1, mock_update_worker_model)
    assert result.id is not None, "update worker method must return update id"

    with pytest.raises(Exception) as e:
        await mock_worker_service.update_one(2, mock_update_worker_model)
        assert 404 in str(e.status_code)
    

    
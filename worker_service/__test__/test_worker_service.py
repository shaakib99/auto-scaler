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
    
@pytest.mark.asyncio
async def test_get_one(
    mock_worker_service,
    ):
    result = await mock_worker_service.get_one(1)
    assert result.id is not None, "get one worker method must return id"

    with pytest.raises(Exception) as e:
        await mock_worker_service.get_one(2)
        assert 404 in str(e.status_code)

@pytest.mark.asyncio
async def test_get_all(
    mock_worker_service,
    ):
    result = await mock_worker_service.get_all(1)
    assert len(result) > 0, "get all worker method must return at least one result"

@pytest.mark.asyncio
async def test_delete_one(
    mock_worker_service,
    ):
    result = await mock_worker_service.delete_one(1)
    assert result is None, "get all worker method must delete"

    with pytest.raises(Exception) as e:
        await mock_worker_service.delete_one(2)
        assert 404 in str(e.status_code)
    

    
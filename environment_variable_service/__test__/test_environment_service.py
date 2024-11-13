import pytest
from environment_variable_service.__test__.mocks import *

@pytest.mark.asyncio
async def test_create_one(mock_environment_variable_service, mock_create_environment_variable_model):
    result = await mock_environment_variable_service.create_one(mock_create_environment_variable_model)
    assert result.id is not None, "Should create environment variable"

    mock_create_environment_variable_model.worker_id = 2
    with pytest.raises(Exception) as e:
        result = await mock_environment_variable_service.create_one(mock_create_environment_variable_model)
        assert e.status_code == 404, "worker id should not be found"
    
@pytest.mark.asyncio
async def test_update_one(mock_environment_variable_service, mock_update_environment_variable_model):
    result = await mock_environment_variable_service.update_one(id=1, data=mock_update_environment_variable_model)
    assert result.id is not None, "Should update environment variable"

    with pytest.raises(Exception) as e:
        result = await mock_environment_variable_service.update_one(2, mock_update_environment_variable_model)
        assert e.status_code == 404, "environment variable id should not be found"

@pytest.mark.asyncio
async def test_get_one(mock_environment_variable_service):
    result = await mock_environment_variable_service.get_one(id=1)
    assert result.id is not None, "Should get environment variable"

    with pytest.raises(Exception) as e:
        result = await mock_environment_variable_service.get_one(2)
        assert e.status_code == 404, "environment variable id should not be found"

@pytest.mark.asyncio
async def test_delete_one(mock_environment_variable_service):
    result = await mock_environment_variable_service.delete_one(id=1)
    assert result is None, "Should delete environment variable"

    with pytest.raises(Exception) as e:
        result = await mock_environment_variable_service.delete_one(2)
        assert e.status_code == 404, "environment variable id should not be found"

@pytest.mark.asyncio
async def test_get_all(mock_environment_variable_service):
    result = await mock_environment_variable_service.get_all({})
    assert len(result) > 0, "Should get atleast 1 environment variable"
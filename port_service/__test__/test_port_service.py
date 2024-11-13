import pytest
from port_service.__test__.mocks import *

@pytest.mark.asyncio
async def test_create_one(mock_port_service, mock_create_port_model):
    result = await mock_port_service.create_one(mock_create_port_model)
    assert result.id is not None, "Should create port"

    mock_create_port_model.worker_id = 2
    with pytest.raises(Exception) as e:
        result = await mock_port_service.create_one(mock_create_port_model)
        assert e.status_code == 404, "worker id should not be found"
    
@pytest.mark.asyncio
async def test_update_one(mock_port_service, mock_update_port_model):
    result = await mock_port_service.update_one(id=1, data=mock_update_port_model)
    assert result.id is not None, "Should update port"

    with pytest.raises(Exception) as e:
        result = await mock_port_service.update_one(2, mock_update_port_model)
        assert e.status_code == 404, "port id should not be found"

@pytest.mark.asyncio
async def test_get_one(mock_port_service):
    result = await mock_port_service.get_one(id=1)
    assert result.id is not None, "Should get port"

    with pytest.raises(Exception) as e:
        result = await mock_port_service.get_one(2)
        assert e.status_code == 404, "port id should not be found"

@pytest.mark.asyncio
async def test_delete_one(mock_port_service):
    result = await mock_port_service.delete_one(id=1)
    assert result is None, "Should delete port"

    with pytest.raises(Exception) as e:
        result = await mock_port_service.delete_one(2)
        assert e.status_code == 404, "port id should not be found"

@pytest.mark.asyncio
async def test_get_all(mock_port_service):
    result = await mock_port_service.get_all({})
    assert len(result) > 0, "Should get atleast 1 port"
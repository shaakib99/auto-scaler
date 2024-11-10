from unittest.mock import MagicMock, patch
from worker_service.__test__.mocks import mock_create_worker_model, mock_worker_service
from database_service.__test__.mocks import mock_database_service, db_instance
from docker_service.__test__.mocks import mock_docker_service
from port_service.__test__.mocks import mock_port_service, mock_port_schema
from environment_variable_service.__test__.mocks import mock_environment_variable_service, mock_environment_variable_schema
import pytest

@pytest.mark.asyncio
async def test_create_one(
    mock_worker_service,
    mock_create_worker_model
    ):
    pass
    result = await mock_worker_service.create_one(mock_create_worker_model)
    assert result.id is not None, "create worker method must return insert id"

    
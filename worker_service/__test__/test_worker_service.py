from unittest.mock import MagicMock, patch
import pytest
from worker_service.service import WorkerService
from database_service.__test__.mocks import db_instance
from worker_service.__test__.mocks import mock_create_worker_model, mock_worker_service

@pytest.mark.asyncio
async def test_create_one(
    mock_worker_service,
    mock_create_worker_model
    ):
    result = await mock_worker_service.create_one(mock_create_worker_model)

    
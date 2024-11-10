from database_service.service import DatabaseService
from database_service.__test__.mocks import MockSchema, db_instance
import pytest

@pytest.fixture
def mock_database_service(db_instance):
    service = DatabaseService(schema=MockSchema, database=db_instance)
    return service
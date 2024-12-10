import pytest
from fastapi import Request

@pytest.fixture
def mock_request():
    fake_request = Request(
            scope={
                "type": "http",
                "headers": [(b"x-request-token", b"2345")],
            }
        )
    return fake_request

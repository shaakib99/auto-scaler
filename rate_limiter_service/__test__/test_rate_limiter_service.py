import pytest
from rate_limiter_service.__test__.mocks import *
from common.exceptions import TooManyRequestsException

@pytest.mark.asyncio
async def test_rate_limiter_service(mock_rate_limiter_service, mock_request):
    max_tokens = 10
    for i in range(max_tokens):
        result = await mock_rate_limiter_service.token_bucket_algorithm(
            mock_request,
            max_tokens = 10,
            refil_time_in_seconds = 60
        )
        assert result is not None, 'Should allow request'
    
    with pytest.raises(TooManyRequestsException) as e:
        result = await mock_rate_limiter_service.token_bucket_algorithm(
            mock_request,
            max_tokens = 10,
            refil_time_in_seconds = 60
        )
        assert e.message == 'Too Many Request'


from fastapi import Request
from cache_service.service import CacheService
from rate_limiter_service.models import TokenBucketParamModel
import json
from datetime import datetime
from common.exceptions import TooManyRequestsException
class RateLimiterService:
    def __init__(self, cache_service: CacheService = None):
        self.cache_service = cache_service or CacheService()

    def token_bucket_algorithm(self, request: Request, max_token: int = 10, refil_time: int = 30, **kwargs):
        headers = request.headers
        token = headers.get("token")
        
        key = f"rate_limiter:{token}"
        result_str = self.cache_service.get(key)
        
        if result_str is None:
            result = TokenBucketParamModel(available_tokens=max_token, last_updated_time=datetime.now())
            result.available_tokens = max_token
            result.last_updated_time = datetime.now()
            self.cache_service.set(key, result.model_dump().__str__(), expire=refil_time)
            return result

        result = TokenBucketParamModel.model_validate(json.loads(result_str))
        if result.available_tokens > 0:
            result.available_tokens -= 1
            self.cache_service.set(key, result.model_dump().__str__(), expire=refil_time)
        else:
            if (datetime.now() -  result.last_updated_time).min < refil_time:
                raise TooManyRequestsException(message="Too many requests")
            else:
                result.available_tokens = max_token
                result.last_updated_time = datetime.now()
                self.cache_service.set(key, result.model_dump().__str__(), expire=refil_time)

        return result


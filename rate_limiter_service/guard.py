from rate_limiter_service.service import RateLimiterService

class RateLimiterGuard:
    def __init__(self, rate_limiter_service: "RateLimiterService" = RateLimiterService()):
        self.rate_limiter_service = rate_limiter_service
    
    async def __call__(self, *args, **kwargs):
        request = kwargs.get("request")
        assert request is not None, "Must add request in router"
        await self.rate_limiter_service.token_bucket_algorithm(request)
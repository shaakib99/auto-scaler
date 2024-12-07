from rate_limiter_service.service import RateLimiterService

class RateLimiterGuard:
    def __init__(self, rate_limiter_service: "RateLimiterService" = RateLimiterService()):
        self.rate_limiter_service = rate_limiter_service
    
    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        request = args[0]
        self.rate_limiter_service.token_bucket_algorithm(request)
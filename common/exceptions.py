from fastapi.exceptions import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, message = 'Not Found'):
        super().__init__(status_code=404, detail=message)

class BadRequestException(HTTPException):
    def __init__(self, message = 'Bad Request'):
        super().__init__(status_code=400, detail=message)

class ForbiddenException(HTTPException):
    def __init__(self, message = 'Forbidden'):
        super().__init__(status_code=403, detail=message)

class UnauthorizedException(HTTPException):
    def __init__(self, message = 'Unauthorized'):
        super().__init__(status_code=401, detail=message)

class TooManyRequestsException(HTTPException):
    def __init__(self, message = 'Too Many Requests'):
        super().__init__(status_code=429, detail=message)
from fastapi.exceptions import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, message = "Not Found"):
        super(status_code = 404, message = message)
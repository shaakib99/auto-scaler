from fastapi.exceptions import HTTPException

class NotFoundException(HTTPException):
    def __init__(self, message = "Not Found"):
        super().__init__(status_code=404, detail=message)
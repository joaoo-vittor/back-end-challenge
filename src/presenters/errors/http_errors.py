class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_422():
        """HTTP 422"""

        return ModelError(status_code=422, body={"error": "Unprecessable Entity"})

    @staticmethod
    def error_400():
        """HTTP 400"""

        return ModelError(status_code=400, body={"error": "Bad Request"})

    @staticmethod
    def error_409():
        """HTTP 409"""

        return ModelError(status_code=409, body={"error": "Conflict"})

    @staticmethod
    def error_500():
        """HTTP 500"""

        return ModelError(status_code=500, body={"error": "Internal Server Error"})


class ModelError:
    def __init__(self, status_code: int, body: dict) -> None:
        self.status_code = status_code
        self.body = body

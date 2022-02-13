from typing import Type
from src.main.interface import RouterInterface
from src.domain.usecases.delete_space_flight import DeleteSpaceFlightUseCase
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class DeleteSpaceFlightController(RouterInterface):
    """Class to define Route to delete space flight controller"""

    def __init__(
        self, delete_space_flight_use_case: Type[DeleteSpaceFlightUseCase]
    ) -> None:
        self.delete_space_flight_use_case = delete_space_flight_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """method to call use case"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "id" in body_params:
                id = http_request.body["id"]
                response = self.delete_space_flight_use_case.delete_by(id=id)

            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

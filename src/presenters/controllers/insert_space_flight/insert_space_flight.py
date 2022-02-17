from typing import Type
from src.main.interface import RouterInterface
from src.domain.interfaces.insert_space_flight import InsertSpaceFlightUseCaseInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.utils.validators import validate_data_space_flight


class InsertSpaceFlightController(RouterInterface):
    def __init__(
        self, insert_space_flight_use_case: Type[InsertSpaceFlightUseCaseInterface]
    ) -> None:
        self.insert_space_flight_use_case = insert_space_flight_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        response = None

        if http_request.body:

            body_params_is_valid = validate_data_space_flight(http_request.body)

            if body_params_is_valid:
                response = self.insert_space_flight_use_case.insert_one(
                    data=http_request.body
                )

            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error.status_code, body=http_error.body
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(status_code=http_error.status_code, body=http_error.body)

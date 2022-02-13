from typing import Type
from src.main.interface import RouterInterface
from src.domain.interfaces.update_space_flight import UpdateSpaceFlightUseCaseInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.utils.validators import validate_data_to_update_space_flight


class UpdateSpaceFlightController(RouterInterface):
    def __init__(
        self, update_space_flight_use_case: Type[UpdateSpaceFlightUseCaseInterface]
    ) -> None:
        self.update_space_flight_use_case = update_space_flight_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        response = None

        if http_request.body:

            body_params_is_valid = validate_data_to_update_space_flight(
                http_request.body
            )

            if body_params_is_valid:
                id = http_request.body["id"]
                data = http_request.body["data"]
                response = self.update_space_flight_use_case.update_by(id=id, data=data)

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

from typing import Type
from src.main.interface import RouterInterface
from src.domain.interfaces.find_space_flight import (
    FindSpaceFlightUseCaseInterface,
)
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors
from src.utils.validators import validate_limit_and_skip


class FindSpaceFlightController(RouterInterface):
    def __init__(
        self, find_space_flight_use_case: Type[FindSpaceFlightUseCaseInterface]
    ) -> None:
        self.find_space_flight_use_case = find_space_flight_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        response = None

        if http_request.query:

            body_params_is_valid = validate_limit_and_skip(http_request.query)
            if body_params_is_valid:
                limit_page = http_request.query["limit_page"]
                skip_page = http_request.query["skip_page"]
                response = self.find_space_flight_use_case.find_by(
                    limit_page=limit_page, skip_page=skip_page
                )
            else:
                response = {"success": False, "data": None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=response["status_code"], body=response["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

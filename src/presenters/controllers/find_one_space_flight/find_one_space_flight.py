from typing import Type
from src.main.interface import RouterInterface
from src.domain.interfaces.find_one_space_flight import (
    FindOneSpaceFlightUseCaseInterface,
)
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindOneSpaceFlightController(RouterInterface):
    def __init__(
        self, find_one_space_flight_use_case: Type[FindOneSpaceFlightUseCaseInterface]
    ) -> None:
        self.find_one_space_flight_use_case = find_one_space_flight_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "id" in body_params:
                id = http_request.body["id"]
                response = self.find_one_space_flight_use_case.find_one_by(id)

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

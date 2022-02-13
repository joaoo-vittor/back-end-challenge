from typing import Dict
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class FindSpaceFlightUseCaseSpy:
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository
        self.params_find_by_limit_page = None
        self.params_find_by_skip_page = None

    def find_by(self, limit_page: int = None, skip_page: int = None) -> Dict:
        if not limit_page:
            raise MissingParamError("limit_page")

        if not skip_page:
            raise MissingParamError("skip_page")

        self.params_find_by_limit_page = limit_page
        self.params_find_by_skip_page = skip_page

        data = None

        is_valid = isinstance(skip_page, int) and isinstance(limit_page, int)

        if is_valid:
            data = self.space_flight_repository.find(limit_page, skip_page)

        if data:
            return {"success": True, "data": data}
        return {"success": False, "data": None}

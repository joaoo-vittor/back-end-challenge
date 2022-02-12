from typing import Dict
from src.domain.interfaces import FindOneSpaceFlightUseCaseInterface
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class FindOneSpaceFlightUseCase(FindOneSpaceFlightUseCaseInterface):
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository

    def find_one_by(self, id: int = None) -> Dict:
        if not id:
            raise MissingParamError("id")

        data = None

        is_valid = isinstance(id, int)

        if is_valid:
            data = self.space_flight_repository.find_one(id)

        if data:
            return {"success": True, "data": data}
        return {"success": False, "data": None}

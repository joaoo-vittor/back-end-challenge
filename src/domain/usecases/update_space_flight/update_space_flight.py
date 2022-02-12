from typing import Dict
from src.domain.interfaces import UpdateSpaceFlightUseCaseInterface
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class UpdateSpaceFlightUseCase(UpdateSpaceFlightUseCaseInterface):
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository

    def update_by(self, id: int = None, data: dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        if not id:
            raise MissingParamError("id")

        response = self.space_flight_repository.update(id=id, data=data)

        if response:
            return {"success": True, "data": response}
        return {"success": False, "data": None}

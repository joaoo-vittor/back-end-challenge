from typing import Dict
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class UpdateSpaceFlightUseCaseSpy:
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository
        self.param_update_by_id = None
        self.param_update_by_data = None

    def update_by(self, id: int = None, data: dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        if not id:
            raise MissingParamError("id")

        self.param_update_by_id = id
        self.param_update_by_data = data

        response = self.space_flight_repository.update(id=id, data=data)

        if response:
            return {"success": True, "data": response}
        return {"success": False, "data": None}

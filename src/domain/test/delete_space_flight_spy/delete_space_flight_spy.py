from typing import Dict
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class DeleteSpaceFlightUseCaseSpy:
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository
        self.param_delete_by_id = None

    def delete_by(self, id: int = None) -> Dict:
        if not id:
            raise MissingParamError("id")

        self.param_delete_by_id = id

        data = None

        is_valid = isinstance(id, int)

        if is_valid:
            data = self.space_flight_repository.delete(id)

        if data:
            return {"success": True, "data": data}
        return {"success": False, "data": None}

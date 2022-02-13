from typing import Dict
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class InsertSpaceFlightUseCaseSpy:
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository
        self.param_insert_one_data = None

    def insert_one(self, data: dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        self.param_insert_one_data = data
        response = self.space_flight_repository.insert(data)

        if response:
            return {"success": True, "data": response}
        return {"success": False, "data": None}

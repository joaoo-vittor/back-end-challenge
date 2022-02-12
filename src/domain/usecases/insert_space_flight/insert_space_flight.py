from typing import Dict
from src.domain.interfaces import InsertSpaceFlightUseCaseInterface
from src.infra.interfaces import (
    SpaceFlightNewInterfaceRepository as SpaceFlightNewRepository,
)
from src.utils.errors import MissingParamError


class InsertSpaceFlightUseCase(InsertSpaceFlightUseCaseInterface):
    def __init__(self, space_flight_repository: SpaceFlightNewRepository) -> None:
        self.space_flight_repository = space_flight_repository

    def insert_one(self, data: dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        response = self.space_flight_repository.insert(data)

        if response:
            return {"success": True, "data": response}
        return {"success": False, "data": None}

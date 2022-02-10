from typing import Dict
from src.infra.interfaces import SpaceFlightNewInterfaceRepository
from src.utils.errors import MissingParamError


class SpaceFlightNewRepository(SpaceFlightNewInterfaceRepository):
    def insert(self, data: Dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

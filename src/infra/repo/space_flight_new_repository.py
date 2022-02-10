from typing import Dict
from src.infra.interfaces import SpaceFlightNewInterfaceRepository
from src.utils.errors import MissingParamError
from src.infra.config import DBConnectionHandler


class SpaceFlightNewRepository(SpaceFlightNewInterfaceRepository):
    def insert(self, data: Dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        try:
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                inserted_space_flight = collection.insert_one(data)

            return inserted_space_flight
        except:
            raise Exception("server error")

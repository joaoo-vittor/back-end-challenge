from typing import Dict, List
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

    def find(self, limit_page: int, skip_page: int) -> List[Dict]:
        try:
            space_flights = None
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                skips = limit_page * (skip_page - 1)
                space_flights = [
                    i for i in collection.find().skip(skips).limit(limit_page)
                ]
            return space_flights
        except:
            raise Exception("Server error")

    def find_one(self, id: int = None) -> Dict:
        print("")

    def update(self, id: int = None, data: Dict = None) -> Dict:
        print("")

    def delete(self, id: int = None) -> bool:
        print("")

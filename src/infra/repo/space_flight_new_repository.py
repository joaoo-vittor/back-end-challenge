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

            return {"inserted_id": str(inserted_space_flight.inserted_id)}
        except:
            raise Exception("server error")

    def find(self, limit_page: int, skip_page: int) -> List[Dict]:
        try:
            data = None
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                skips = limit_page * (skip_page - 1)
                space_flights = [
                    i for i in collection.find().skip(skips).limit(limit_page)
                ]
                data = [{**i, "_id": str(i["_id"])} for i in space_flights]
            return data
        except:
            raise Exception("Server error")

    def find_one(self, id: int = None) -> Dict:
        try:
            data = None
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                space_flight = collection.find_one({"id": id}, {})
                data = {**space_flight, "_id": str(space_flight["_id"])}

            return data
        except:
            raise Exception("Server error")

    def update(self, id: int = None, data: Dict = None) -> Dict:
        try:
            space_flight = None
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                space_flight = collection.update_one({"id": id}, {"$set": data})
            return {"modified_count": space_flight.modified_count}
        except:
            raise Exception("Server error")

    def delete(self, id: int = None) -> Dict:
        try:
            space_flight = None
            with DBConnectionHandler() as connection:
                collection = connection.get_collection("spaceFlight")
                space_flight = collection.delete_one({"id": id})

            return {"deleted_count": space_flight.deleted_count}
        except:
            raise Exception("Server error")

from pymongo import MongoClient
from pymongo.collection import Collection
from src.settings import MONGO_ATLAS_URL


class DBConnectionHandler:
    """Connection with Mongo Client"""

    def __init__(self) -> None:
        self.__connection_string = MONGO_ATLAS_URL
        self.client = None

    def __get_db(self) -> MongoClient:
        self.client = MongoClient(self.__connection_string)
        return self.client["ChallengeCoodesh"]

    def get_collection(self, collection_name: str) -> Collection:
        db = self.__get_db()
        return db[collection_name]

    def disconnect(self) -> None:
        self.client.close()

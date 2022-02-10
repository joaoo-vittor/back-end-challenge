from pymongo import MongoClient
from pymongo.collection import Collection
from src.settings import MONGO_ATLAS_URL


class DBConnectionHandler:
    """Connection with Mongo Client"""

    def __init__(self) -> None:
        self.__connection_string = MONGO_ATLAS_URL
        self.client = None
        self.db = None

    def get_collection(self, collection_name: str) -> Collection:
        self.db = self.client["ChallengeCoodesh"]
        return self.db[collection_name]

    def __enter__(self):
        self.client = MongoClient(
            self.__connection_string, tls=True, tlsAllowInvalidCertificates=True
        )
        self.db = self.client["ChallengeCoodesh"]
        return self

    def __exit__(self, exe_type, exe_val, exc_tb):
        self.client.close()

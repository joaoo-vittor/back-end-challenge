from typing import Dict, List
from src.utils.errors import MissingParamError
from .mocks import mock_list_space_flight, mock_one_space_flight


class SpaceFlightNewRepository:
    def insert(self, data: Dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")

        return {"inserted_id": "ncown98h13duqu21"}

    def find(self, limit_page: int, skip_page: int) -> List[Dict]:
        return mock_list_space_flight

    def find_one(self, id: int = None) -> Dict:
        return mock_one_space_flight

    def update(self, id: int = None, data: Dict = None) -> Dict:
        return {"modified_count": 1}

    def delete(self, id: int = None) -> bool:
        return {"deleted_count": 1}

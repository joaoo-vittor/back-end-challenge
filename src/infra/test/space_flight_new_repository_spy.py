from typing import Dict, List
from src.utils.errors import MissingParamError
from .mocks import mock_list_space_flight, mock_one_space_flight


class SpaceFlightNewRepositorySpy:
    def __init__(self) -> None:
        self.param_inserted_data = {}
        self.param_find_limit_page = None
        self.param_find_skip_page = None
        self.param_find_one_id = None
        self.param_update_id = None
        self.param_update_data = None
        self.param_delete_id = None

    def insert(self, data: Dict = None) -> Dict:
        if not data:
            raise MissingParamError("data")
        self.param_inserted_data = data
        return {"inserted_id": "ncown98h13duqu21"}

    def find(self, limit_page: int, skip_page: int) -> List[Dict]:
        self.param_find_limit_page = limit_page
        self.param_find_skip_page = skip_page
        return mock_list_space_flight

    def find_one(self, id: int = None) -> Dict:
        self.param_find_one_id = id
        return mock_one_space_flight

    def update(self, id: int = None, data: Dict = None) -> Dict:
        self.param_update_id = id
        self.param_update_data = data
        return {"modified_count": 1}

    def delete(self, id: int = None) -> Dict:
        self.param_delete_id = id
        return {"deleted_count": 1}

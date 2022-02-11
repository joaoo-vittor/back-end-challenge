from abc import ABC, abstractmethod
from typing import Dict, List


class SpaceFlightNewInterfaceRepository(ABC):
    @abstractmethod
    def insert(self, data: Dict = None) -> Dict:
        raise Exception("Implements: insert method")

    @abstractmethod
    def find_one(self, id: int = None) -> Dict:
        raise Exception("Implements: find_one method")

    @abstractmethod
    def find(self, limit_page: int, skip_page: int) -> List[Dict]:
        raise Exception("Implements: find method")

    @abstractmethod
    def update(self, id: int = None, data: Dict = None) -> Dict:
        raise Exception("Implements: update method")

    @abstractmethod
    def delete(self, id: int = None) -> bool:
        raise Exception("Implements: delete method")

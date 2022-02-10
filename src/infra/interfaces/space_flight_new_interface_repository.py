from abc import ABC, abstractmethod
from typing import Dict


class SpaceFlightNewInterfaceRepository(ABC):
    @abstractmethod
    def insert(self, data: Dict = None) -> Dict:
        raise Exception("Implements: insert method")

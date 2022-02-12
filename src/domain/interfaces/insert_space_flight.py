from abc import ABC, abstractmethod
from typing import Dict


class InsertSpaceFlightUseCaseInterface(ABC):
    """Insert Space Flight UseCase"""

    @abstractmethod
    def insert_one(self, data: dict = None) -> Dict:
        raise Exception("Implements method: insert one")

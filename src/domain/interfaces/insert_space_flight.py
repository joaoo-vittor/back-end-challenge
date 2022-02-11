from abc import ABC, abstractmethod
from typing import Dict


class InsertSpaceFlightUseCase(ABC):
    """Insert Space Flight UseCase"""

    @abstractmethod
    def insert_one(self, data: dict) -> Dict:
        raise Exception("Implements method: insert one")

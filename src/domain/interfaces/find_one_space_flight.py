from abc import ABC, abstractmethod
from typing import Dict


class FindOneSpaceFlightUseCaseInterface(ABC):
    """Find One Space Flight UseCase"""

    @abstractmethod
    def find_one_by(self, id: int = None) -> Dict:
        raise Exception("Implements method: find one by id")

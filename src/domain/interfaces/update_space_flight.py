from abc import ABC, abstractmethod
from typing import Dict


class UpdateSpaceFlightUseCaseInterface(ABC):
    """Update Space Flight UseCase"""

    @abstractmethod
    def update_by(self, id: int, data: dict) -> Dict:
        raise Exception("Implements method: update by limit page and skip page")

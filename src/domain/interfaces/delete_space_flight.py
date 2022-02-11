from abc import ABC, abstractmethod
from typing import Dict


class DeleteSpaceFlightUseCaseInterface(ABC):
    """Delete Space Flight UseCase"""

    @abstractmethod
    def delete_by(self, id: int) -> Dict:
        raise Exception("Implements method: delete by id")

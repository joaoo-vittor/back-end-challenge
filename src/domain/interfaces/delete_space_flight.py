from abc import ABC, abstractmethod
from typing import Dict


class DeleteSpaceFlightUseCase(ABC):
    """Delete Space Flight UseCase"""

    @abstractmethod
    def delete_by(self, id: int) -> Dict:
        raise Exception("Implements method: delete by id")

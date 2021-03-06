from abc import ABC, abstractmethod
from typing import Dict, List


class FindSpaceFlightUseCaseInterface(ABC):
    """Find Space Flight UseCase"""

    @abstractmethod
    def find_by(self, limit_page: int = None, skip_page: int = None) -> List[Dict]:
        raise Exception("Implements method: find by limit page and skip page")

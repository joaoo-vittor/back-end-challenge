from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouterInterface(ABC):
    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Interface to Routes

        Args:
            http_request (Type[HttpRequest]): http request

        Returns:
            HttpResponse: http response
        """

        raise Exception("Should implement method: route")

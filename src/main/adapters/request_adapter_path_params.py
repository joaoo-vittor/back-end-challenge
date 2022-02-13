from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


def request_adapter_path_params(request: RequestFastApi, callback: Callable):
    """Adapter to httpRequest

    Args:
        request (request): Http request object with all properties
        callback (callback): Callback to process http request
    """

    body = None

    try:
        body = {"id": int(request.path_params["id"])}
    except:
        pass

    http_request = HttpRequest(body=body)

    http_response = callback(http_request)
    return http_response

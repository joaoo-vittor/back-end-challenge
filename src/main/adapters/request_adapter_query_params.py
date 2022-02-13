from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


def request_adapter_query_params(request: RequestFastApi, callback: Callable):
    """Adapter to httpRequest

    Args:
        request (request): Http request object with all properties
        callback (callback): Callback to process http request
    """

    query_params = None

    try:
        query_params = {
            "limit_page": int(request.query_params["limit_page"]),
            "skip_page": int(request.query_params["skip_page"]),
        }
    except:
        pass

    http_request = HttpRequest(query=query_params)
    http_response = callback(http_request)
    return http_response

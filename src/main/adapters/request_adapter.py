from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


async def request_adapter(request: RequestFastApi, callback: Callable):
    """Adapter to httpRequest

    Args:
        request (request): Http request object with all properties
        callback (callback): Callback to process http request
    """

    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = HttpRequest(body=body)

    http_response = callback(http_request)
    return http_response

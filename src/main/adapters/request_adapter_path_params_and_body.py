from typing import Callable
from fastapi import Request as RequestFastApi
from src.presenters.helpers import HttpRequest


async def request_adapter_path_params_and_body(
    request: RequestFastApi, callback: Callable
):
    """Adapter to httpRequest

    Args:
        request (request): Http request object with all properties
        callback (callback): Callback to process http request
    """

    data = None

    try:
        body = await request.json()
        data = {"id": int(request.path_params["id"]), "data": body}
    except:
        pass

    http_request = HttpRequest(body=data)

    http_response = callback(http_request)
    return http_response

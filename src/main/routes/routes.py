from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.main.compose import (
    insert_space_flight_compose,
    find_space_flight_compose,
    find_one_space_flight_compose,
    update_space_flight_compose,
    delete_space_flight_compose,
)
from src.main.adapters import (
    request_adapter,
    request_adapter_query_params,
    request_adapter_path_params,
    request_adapter_path_params_and_body,
)
from src.presenters.errors import HttpErrors
from json import loads, dumps

routes = APIRouter()


def parse_json(data: dict):
    return loads(dumps(data))


@routes.get("/")
def index(request: RequestFastApi):
    return JSONResponse(
        content={"msg": "Back-end Challenge 2021 🏅 - Space Flight News"}
    )


@routes.post("/articles")
async def insert_article(request: RequestFastApi):
    controller = insert_space_flight_compose()
    response = None

    try:
        response = await request_adapter(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )


@routes.get("/articles")
async def find_articles(request: RequestFastApi):
    controller = find_space_flight_compose()
    response = None
    try:
        response = request_adapter_query_params(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )


@routes.get("/articles/{id}")
async def find_one_article(request: RequestFastApi):
    controller = find_one_space_flight_compose()
    response = None
    try:
        response = request_adapter_path_params(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )


@routes.put("/articles/{id}")
async def find_one_article(request: RequestFastApi):
    controller = update_space_flight_compose()
    response = None
    try:
        response = await request_adapter_path_params_and_body(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )


@routes.delete("/articles/{id}")
async def find_one_article(request: RequestFastApi):
    controller = delete_space_flight_compose()
    response = None
    try:
        response = request_adapter_path_params(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content=response.body,
    )

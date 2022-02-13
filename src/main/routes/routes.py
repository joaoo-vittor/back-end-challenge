from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.main.compose import insert_space_flight_compose
from src.main.adapters import request_adapter
from src.presenters.errors import HttpErrors

routes = APIRouter()


@routes.get("/")
def index(request: RequestFastApi):
    return JSONResponse(
        content={"msg": "Back-end Challenge 2021 🏅 - Space Flight News"}
    )


@routes.post("/articles/")
async def index(request: RequestFastApi):
    controller = insert_space_flight_compose()
    response = None

    try:
        response = await request_adapter(request, controller.route)
    except Exception as e:
        response = HttpErrors.error_500()

    return JSONResponse(
        status_code=response.status_code,
        content={"inserted_id": str(response.body.inserted_id)},
    )

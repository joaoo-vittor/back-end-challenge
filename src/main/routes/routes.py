from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

routes = APIRouter()


@routes.get("/")
def index(request: RequestFastApi):
    return JSONResponse(
        content={"msg": "Back-end Challenge 2021 🏅 - Space Flight News"}
    )

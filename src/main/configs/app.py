from fastapi import FastAPI
from src.main.routes import routes
from fastapi.staticfiles import StaticFiles

api = FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")
api.openapi_url = "/static/swagger.yml"

api.include_router(routes)

from fastapi import FastAPI
from src.main.configs.doc import custom_openapi
from src.main.routes import routes

api = FastAPI(docs_url="/doc")


def openapi():
    return custom_openapi(api)


api.openapi = openapi

api.include_router(routes)

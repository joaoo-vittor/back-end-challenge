from fastapi import FastAPI
from src.main.routes import routes

api = FastAPI()

api.include_router(routes)

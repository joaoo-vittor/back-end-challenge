import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_ATLAS_URL = os.environ.get("MONGO_ATLAS_URL")

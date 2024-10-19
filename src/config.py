import os

from dotenv import load_dotenv

load_dotenv()

MISTRAL_KEY = os.environ["MISTRAL_API_KEY"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_DB_NAME = os.environ["MONGO_DB_NAME"]
MONGO_COLLECTION_NAME = os.environ["MONGO_COLLECTION_NAME"]
MONGO_LOGIN = os.environ["MONGO_LOGIN"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]

static_config = {"mistral_key": MISTRAL_KEY}

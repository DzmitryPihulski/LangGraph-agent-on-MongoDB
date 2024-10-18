import os

from dotenv import load_dotenv

load_dotenv()

MISTRAL_KEY = os.environ["MISTRAL_API_KEY"]

static_config = {"mistral_key": MISTRAL_KEY}

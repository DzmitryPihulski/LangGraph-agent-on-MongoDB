import json
import urllib.request
from typing import Literal

from db.db import airbnb_db


async def fetch_sample_data() -> Literal[True]:
    url = "https://raw.githubusercontent.com/neelabalan/mongodb-sample-dataset/refs/heads/main/sample_airbnb/listingsAndReviews.json"
    response = await urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    json_objects = data.strip().split("\n")
    parsed_data = [json.loads(obj) for obj in json_objects]
    airbnb_db.collection.insert_many(documents=parsed_data)
    return True

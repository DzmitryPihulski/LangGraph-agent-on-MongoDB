import json
import urllib.request
from typing import Dict, List, Literal, Union

from db.db import airbnb_db


def replace_dollar_keys(obj: Union[Dict, List, str]) -> Union[Dict, str]:  # type: ignore
    """
    Deletes the dollar sign from the source data.

    Args:
        obj (Dict): the data.

    Returns:
        Dict: formed data.
    """
    if isinstance(obj, dict):
        # Iterate over the keys and values in the dictionary
        for key, value in list(obj.items()):  # type: ignore
            if isinstance(value, dict) and len(value) == 1:  # type: ignore
                inner_key = next(iter(value))  # type: ignore
                # Recursively handle nested "$" keys
                if inner_key.startswith("$"):  # type: ignore
                    obj[key] = replace_dollar_keys(value[inner_key])  # type: ignore
                else:
                    # Recur if inner dictionary doesn't match criteria
                    replace_dollar_keys(value)
            else:
                replace_dollar_keys(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):  # type: ignore
            obj[i] = replace_dollar_keys(obj[i])  # type: ignore
    return obj  # type: ignore


async def fetch_sample_data() -> Literal[True]:
    """Fetches the documents from the source page and
    adds to the database in the working collection.

    Returns:
        Literal[True]: whether the operation succeeded.
    """
    url = "https://raw.githubusercontent.com/neelabalan/mongodb-sample-dataset/refs/heads/main/sample_airbnb/listingsAndReviews.json"
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    json_objects = data.strip().split("\n")
    parsed_data = [  # type: ignore
        replace_dollar_keys(replace_dollar_keys(json.loads(obj)))
        for obj in json_objects
    ]
    airbnb_db.collection.insert_many(documents=parsed_data)  # type: ignore
    return True

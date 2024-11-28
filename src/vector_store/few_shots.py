from dataclasses import dataclass
from typing import Dict, Union


@dataclass
class Shot:
    """
    Data class representing a shot to be stored in the vector store.
    That will be used to create fewshots prompts.

    Attributes:
        human_input (str): The query of the human
        tool_call (dict): The dict of the tool calls
    """

    human_input: str
    tool_call: Dict[str, Dict[str, Union[str, int, bool]]]


MONGO_SHOTS = [
    Shot(
        human_input="Shom me number of bedrooms of property with url https://www.airbnb.com/rooms/10006546",
        tool_call={
            "filter": {"listing_url": "https://www.airbnb.com/rooms/10006546"},
            "projection": {"listing_url": 1, "bedrooms": 1},
        },
    ),
    Shot(
        human_input="Show me all apartments with 6 bedrooms.",
        tool_call={
            "filter": {"bedrooms": "7"},
            "projection": {"listing_url": 1, "name": 1, "bedrooms": 1},
        },
    ),
    Shot(
        human_input="Shom me the summary of property Ribeira Charming Duplex",
        tool_call={
            "filter": {"name": "Ribeira Charming Duplex"},
            "projection": {"name": 1, "summary": 1},
        },
    ),
    Shot(
        human_input="Shom me the country of property with id 10009999",
        tool_call={
            "filter": {"_id": "10009999"},
            "projection": {"_id": 1, "address.country": 1},
        },
    ),
    Shot(
        human_input="Shom me the room type of property Horto flat with small garden",
        tool_call={
            "filter": {"name": "Horto flat with small garden"},
            "projection": {"name": 1, "room_type": 1},
        },
    ),
    Shot(
        human_input="Shom me the minimum nights of property Ocean View Waikiki Marina w/prkg",
        tool_call={
            "filter": {"name": "Ocean View Waikiki Marina w/prkg"},
            "projection": {"name": 1, "minimum_nights": 1},
        },
    ),
]

from typing import Annotated
from typing_extensions import TypedDict


class State(TypedDict):
    human_input: Annotated[str, "The initial query."]


class Config(TypedDict):
    langchain_key: Annotated[str, "The key for the LLMs."]

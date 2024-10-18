from typing import Annotated, List

from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class State(TypedDict):
    human_input: Annotated[str, "The initial query."]
    messages: Annotated[
        List[AIMessage | HumanMessage],
        add_messages,
        "Messages between nodes.",
    ]


class Config(TypedDict):
    pass


class InputModel(TypedDict):
    human_input: Annotated[str, "The initial query."]

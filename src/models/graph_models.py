from typing import Annotated, List
from typing_extensions import TypedDict
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.message import add_messages


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

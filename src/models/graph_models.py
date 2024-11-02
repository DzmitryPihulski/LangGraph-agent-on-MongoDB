from typing import Annotated, List, Union

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langgraph.graph.message import add_messages  # type: ignore
from typing_extensions import TypedDict


class State(TypedDict):
    human_input: Annotated[str, "The initial query."]
    messages: Annotated[
        List[Union[AIMessage, HumanMessage, ToolMessage, None]],
        add_messages,
        "Messages between nodes.",
    ]


class Config(TypedDict):
    pass


class InputModel(TypedDict):
    human_input: Annotated[str, "The initial query."]


class OutputModel(TypedDict):
    messages: Annotated[str, "Messages between nodes."]

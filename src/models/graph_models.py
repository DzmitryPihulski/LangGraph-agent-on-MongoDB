from typing import Annotated, List
from typing_extensions import TypedDict
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    human_input: Annotated[str, "The initial query."]
    messages: Annotated[
        List[AIMessage | HumanMessage | ToolMessage],
        add_messages,
        "Messages between nodes.",
    ]


class Config(TypedDict):
    langchain_key: Annotated[str, "The key for the LLMs."]

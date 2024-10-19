import json
from typing import Dict

from fastapi import status
from fastapi.exceptions import HTTPException
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables.config import RunnableConfig
from langchain_core.tools import tool
from langdetect import detect  # type: ignore

from graph.llm import MistralLLM
from models.graph_models import State


def input_validator(
    state: State, config: RunnableConfig
) -> Dict[str, list[HumanMessage]]:
    human_input = state["human_input"].replace("'", "").replace("`", "")
    if (
        detect(state["human_input"]) != "en"
    ):  # The input is not in the english language.
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The input must be in english.",
        )
    return {"messages": [HumanMessage(content=human_input)]}


def exploration_node(
    state: State, config: RunnableConfig
) -> Dict[str, list[AIMessage]]:
    response = MistralLLM.invoke(input=str(state["messages"][-1].content))
    return {"messages": [AIMessage(content=response.content)]}


@tool("mongo_tool")
def mongo_tool():
    """ """
    return None


# CUSTOM TOOL NODE
def customtool_node(
    state: State, config: RunnableConfig
) -> Dict[str, list[ToolMessage | None]]:
    outputs = []
    if isinstance(state["messages"][-1], AIMessage):
        for tool_call in state["messages"][-1].tool_calls:
            tool_result = mongo_tool.invoke(tool_call["args"])
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
    return {"messages": outputs}

from models.graph_models import State
from langdetect import detect  # type: ignore
from langchain_core.runnables.config import RunnableConfig
from fastapi.exceptions import HTTPException
from typing import Dict
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from fastapi import status
from graph.llm import MistralLLM
from langchain_core.tools import tool
import json


def input_validator(state: State, config: RunnableConfig) -> Dict:
    human_input = state["human_input"].replace("'", "").replace("`", "")
    if (
        detect(state["human_input"]) != "en"
    ):  # The input is not in the english language.
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The input must be in english.",
        )
    return {"messages": [HumanMessage(content=human_input)]}


def exploration_node(state: State, config: RunnableConfig) -> Dict:
    response = MistralLLM.invoke(input=state["messages"][-1].content)
    return {"messages": [AIMessage(content=response.content)]}


@tool("mongo_tool")
def mongo_tool():
    """ """
    return None


mongo_tools = [mongo_tool]

tools_by_name = {tool.name: tool for tool in mongo_tools}


# CUSTOM TOOL NODE
def customtool_node(state: State, config: RunnableConfig) -> Dict:
    outputs = []
    if isinstance(state["messages"][-1], AIMessage):
        for tool_call in state["messages"][-1].tool_calls:
            tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )

    return {"messages": outputs}

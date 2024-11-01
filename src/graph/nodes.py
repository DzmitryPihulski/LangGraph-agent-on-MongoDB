import json
from typing import Dict, Union

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.config import RunnableConfig
from langchain_core.tools import tool

from components.prompts import EXPLORATION_AGENT_NODE
from db.db import airbnb_db
from db.scheme import MONGO_DB_SCHEME, SAMPLE_DOCUMENT
from graph.llm import MistralLLM
from models.graph_models import State


def input_validator(
    state: State, config: RunnableConfig
) -> Dict[str, list[HumanMessage]]:
    human_input = state["human_input"].replace("'", "").replace("`", "")
    return {"messages": [HumanMessage(content=human_input)]}


@tool("mongo_tool")
def mongo_tool(filter: Dict, projection: Dict):
    """Exists to execute queries.

    Args:
        filter (Dict)
        projection (Dict)

    Returns:
        list: response
    """
    return list(airbnb_db.collection.find(filter=filter, projection=projection))


# CUSTOM TOOL NODE
def custom_tool_node(
    state: State, config: RunnableConfig
) -> Dict[str, list[Union[ToolMessage, None]]]:
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


def exploration_node(
    state: State, config: RunnableConfig
) -> Dict[str, list[AIMessage]]:
    template = ChatPromptTemplate(
        [
            ("system", EXPLORATION_AGENT_NODE),
            ("human", "{user_query}"),
        ]
    )

    prompt_value = template.invoke(
        {
            "mongo_scheme": MONGO_DB_SCHEME,
            "sample_doc": SAMPLE_DOCUMENT,
            "user_query": str(state["messages"][-1].content),
        }
    )

    llm_with_tools = MistralLLM.bind_tools([mongo_tool])

    response = llm_with_tools.invoke(input=prompt_value)
    return {"messages": [response]}

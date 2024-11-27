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
from vector_store.vector_store import vector_db


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
    outputs = list()
    if isinstance(state["messages"][-1], AIMessage):
        for tool_call in state["messages"][-1].tool_calls:
            arguments = tool_call["args"].copy()
            print("Arguments: ", arguments)
            if "_id" not in arguments["projection"]:
                arguments["projection"]["_id"] = 0
            tool_result = mongo_tool.invoke(arguments, config=config)
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
    return {
        "messages": outputs,
        "answer": str([str(output.content) for output in outputs]),  # type: ignore
    }


def exploration_node(
    state: State, config: RunnableConfig
) -> Dict[str, list[AIMessage]]:
    shots = vector_db.search(str(state["messages"][-1].content))
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
            "few_shot_query_1": HumanMessage(content=shots[0]["text"]).pretty_repr(),
            "few_shot_answer_1": AIMessage(
                content=str(shots[0]["metadata"])
            ).pretty_repr(),
            "few_shot_query_2": HumanMessage(content=shots[1]["text"]).pretty_repr(),
            "few_shot_answer_2": AIMessage(
                content=str(shots[1]["metadata"])
            ).pretty_repr(),
            "few_shot_query_3": HumanMessage(content=shots[2]["text"]).pretty_repr(),
            "few_shot_answer_3": AIMessage(
                content=str(shots[2]["metadata"])
            ).pretty_repr(),
            "few_shot_query_4": HumanMessage(content=shots[3]["text"]).pretty_repr(),
            "few_shot_answer_4": AIMessage(
                content=str(shots[3]["metadata"])
            ).pretty_repr(),
            "few_shot_query_5": HumanMessage(content=shots[4]["text"]).pretty_repr(),
            "few_shot_answer_5": AIMessage(
                content=str(shots[4]["metadata"])
            ).pretty_repr(),
        },
        config=config,
    )

    llm_with_tools = MistralLLM.bind_tools([mongo_tool])
    print("PROMPT FOR RESEARCH LLM:", prompt_value)
    response = llm_with_tools.invoke(input=prompt_value)
    print("RESPONSE: ", response)
    return {"messages": [response]}

from models.graph_models import State, Config
from langdetect import detect  # type: ignore
from fastapi.exceptions import HTTPException
from typing import Dict
from langchain_core.messages import HumanMessage, AIMessage
from fastapi import status
from graph.llm import MistralLLM


def input_validator(state: State, config: Config) -> Dict:
    human_input = state["human_input"].replace("'", "").replace("`", "")
    if (
        detect(state["human_input"]) != "en"
    ):  # The input is not in the english language.
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The input must be in english.",
        )
    return {"messages": [HumanMessage(content=human_input)]}


def exploration_node(state: State, config: Config) -> Dict:
    print("State:", state)
    print("Config:", config)
    response = MistralLLM.invoke(input=state["messages"][-1].content)
    return {"messages": [AIMessage(content=response.content)]}

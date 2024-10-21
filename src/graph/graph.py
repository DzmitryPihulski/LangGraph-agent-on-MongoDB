from langgraph.graph import END, START, StateGraph

from graph.nodes import (  # type: ignore
    custom_tool_node,
    exploration_node,
    input_validator,
)
from models.graph_models import State

graph = StateGraph(state_schema=State)

graph.add_node("Input Validator", input_validator)  # type: ignore
graph.add_node("Exploration Node", exploration_node)  # type: ignore
graph.add_node("MongoDB", custom_tool_node)

graph.add_edge(START, "Input Validator")


def conditional_edge(state: State):
    if state["messages"][-1].tool_calls:
        return "MongoDB"
    return END


graph.add_edge("Input Validator", "Exploration Node")
graph.add_conditional_edges("Exploration Node", conditional_edge)
graph.add_edge("MongoDB", END)

compiled_graph = graph.compile(debug=True)

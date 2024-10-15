from langgraph.graph import StateGraph, START, END
from models.graph_models import State, Config
from graph.nodes import input_validator, exploration_node

graph = StateGraph(state_schema=State, config_schema=Config)

graph.add_node("Input Validator", input_validator)  # type: ignore
graph.add_node("Exploration Node", exploration_node)  # type: ignore

graph.add_edge(START, "Input Validator")
graph.add_edge("Input Validator", "Exploration Node")
graph.add_edge("Exploration Node", END)

compiled_graph = graph.compile()

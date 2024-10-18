from langgraph.graph import END, START, StateGraph

from graph.nodes import exploration_node, input_validator
from models.graph_models import State

graph = StateGraph(state_schema=State)

graph.add_node("Input Validator", input_validator)  # type: ignore
graph.add_node("Exploration Node", exploration_node)  # type: ignore

graph.add_edge(START, "Input Validator")
graph.add_edge("Input Validator", "Exploration Node")
graph.add_edge("Exploration Node", END)

compiled_graph = graph.compile(debug=True)

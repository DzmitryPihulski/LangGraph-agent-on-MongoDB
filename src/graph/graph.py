from langgraph.graph import StateGraph
from src.models.graph_models import State, Config

graph = StateGraph(state_schema=State, config_schema=Config)


compiled_graph = graph.compile()

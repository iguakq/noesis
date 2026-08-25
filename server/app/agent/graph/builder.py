from langgraph.graph import StateGraph

from server.app.agent.graph.nodes.router import router
from server.app.agent.graph.state import State

graph = StateGraph(State)

graph.add_node("router", router)

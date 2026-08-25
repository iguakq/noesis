from typing import Annotated, TypedDict

from langchain.messages import AnyMessage
from langgraph.graph.message import add_messages

class Perm:
  x = 5

class Type:
  x = 5

class Username:
    x = 5



class State(TypedDict):
    # Messages
    # messages: Annotated[list[AnyMessage], Role, Type, Username, add_messages]
    messages: str

    # Qué estábamos haciendo
    # execution_type: str  # "task" | "goal"

    # Goal
    # goal_tasks: list
    # current_task: int

    # Tool dentro de la task
    # current_tool: int

    # Resultado de ejecución
    # results: list

    # Petición que interrumpió
    # pending_request: dict | None

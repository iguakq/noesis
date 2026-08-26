from typing import Annotated, TypedDict

from langchain.messages import AnyMessage


class State(TypedDict):
    # Messages
    messages: list[dict[str, str]]

    # Now
    # execution_type: str  # "task" | "goal"

    # Goal
    goals: list[str]
    # goal_tasks: list
    # current_task: int

    # Tool in task
    tasks: list[str]
    incoming_task : str
    # current_tool: int

    # Result ejecution
    # results: list

    # idk
    # pending_request: dict | None

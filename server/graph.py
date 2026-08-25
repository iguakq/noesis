from langgraph.graph import START, StateGraph


from state import State

from nodes.test import test


builder = StateGraph(State)

builder.add_node("test", test)
builder.set_entry_point("test")
builder.set_finish_point("test")

# builder.add_node("add_task", add_task)
# builder.add_node("answer", answer)
# builder.add_node("executor", executor)
# builder.add_node("planner", planner)
# builder.add_node("response", response)
# builder.add_node("task_router", task_router)

# builder.add_conditional_edges(START, router, {
#         "question": "answer",
#         "task": "add_task",
#         "goal": "planner",
#     })
# builder.add_edge("answer", END)
# builder.add_edge("add_task", "executor")
# builder.add_edge("planner", "executor")
# builder.add_conditional_edges("executor", task_router, {
#         "more": "executor",
#         "done": "response",
#     })
# builder.add_edge("response", END)

graph = builder.compile()

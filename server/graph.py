from pydantic import BaseModel

from agents import answer_agent, router_agent, planner_agent


thread_config = {"configurable": {"thread_id": "1"}}

class Tasks_state(BaseModel):
    tasks: list
    incoming_task: str

tasks_state = Tasks_state

# Route graph based in the perms
def perm_router(message):
    if message.username == "Iguaka": # read username admin list/ if message.username in admin_usernames:
        type_router(message)
    else:
        answer(message)


def type_router(message):
    result = router_agent.invoke({"messages": [{"role": "user", "content": message.content}]})
    classification = result["messages"][-1].content
    print(classification)

    match classification:
        case "QUESTION":
            answer(message)
        case "TASK":
            add_task(message.content)
        case "GOAL":
            planner(message.content)
        case _:
            print("error")


def answer(message):
    status = str # game status info
    goals = str # goal status
    tasks = str # current tasks + incoming task

    result = answer_agent.invoke({"messages": [{"role": "user", "content": message.username + ": " + message.content}]}, thread_config,)
    ai_message = result["messages"][-1]
    print(ai_message.content)

    # send result


def add_task(content):
    tasks_state.incoming_task = content
    print(tasks_state.incoming_task)
    # add message to incoming_task state


def planner(content):
    status = str # get game status

    result = planner_agent.invoke({"messages": [{"role": "user", "content": content}]})

    test = result["messages"][-1].content

    tasks_state.tasks = test
    print(tasks_state.tasks)
    # return tasks
    # save tasks state


async def executor():
        print("A")

        # escuchar cambios en tasks
        # cambio -> empezar a ejecutar
        # terminar todo -> response

        # escuchar cambios en incoming_tasks
        # cambio -> parar task execution, ejecutar
        # resultado -> response


def response():
    print("a")
    # llm call

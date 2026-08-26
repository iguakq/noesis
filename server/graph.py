from langchain.messages import HumanMessage
from langchain.agents import create_agent
from state import State

state: State = {
    "messages": []
}


def perm_router(message):
    state["messages"].append({
        "role": "user",
        "content": message.username + ": " + message.message
    })

    if message.username == "Iguaka": # read username admin list/ if message.username in admin_usernames:
        router(message.message)
    else:
        answer()


def router(message):
    agent = create_agent(
        model="openai:gpt-5.5",
        system_prompt="You are a helpful assistant",
    )
    result = agent.invoke({"messages": [{"role": "user", "content": message}]})

    match result:
        case "question":
            answer()
        case "task":
            add_task(message)
        case "goal":
            planner(message)
        case _:
            print("error")


def answer():
    status = str # game status info
    goals = str # goal status
    tasks = str # current tasks + incoming task

    agent = create_agent(
        model="openai:gpt-5.5",
        system_prompt=f"You are a helpful assistant {status} {goals} {tasks}",
    )
    result = agent.invoke(state["messages"])

    print(result)
    # send result


def add_task(message):
    print("a")
    # add message to incoming_task state


def planner(message):
    status = str # get game status

    agent = create_agent(
        model="openai:gpt-5.5",
        system_prompt=f"You are a helpful assistant {status}",
    )
    result = agent.invoke({"messages": [{"role": "user", "content": message}]})

    # return tasks
    # save tasks state


async def executor():
        print("A")
        print("B")


    # bucle
    # estado1 = false
    # estado2 = false

    # procesoLargo():
    #     mientras siga ejecutándose:

    #         si estado1 cambia a true:
    #             hacer X hasta terminar, si termina mandar respuesta

    #         si estado2 cambia a true:
    #             parar X
    #             hacer Y hasta terminar, volver a x, mandar respuesta


def response():
    print("a")
    # llm call

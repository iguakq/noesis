from config import config

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from promts import ROUTER_SYSTEM_PROMPT,ANSWER_SYSTEM_PROMT, PLANNER_SYSTEM_PROMPT
from langgraph.checkpoint.memory import InMemorySaver

model = init_chat_model(
    config.model,
    temperature=0,
)

router_agent = create_agent(
    model=model,
    system_prompt=ROUTER_SYSTEM_PROMPT,
)

answer_agent = create_agent(
    model=model,
    system_prompt=ANSWER_SYSTEM_PROMT,
    checkpointer=InMemorySaver(),
)

planner_agent = create_agent(
    model=model,
    system_prompt=PLANNER_SYSTEM_PROMPT,
)

response_agent = create_agent(
    model=model,
)

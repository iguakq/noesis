import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from config import config
from graph import executor, perm_router


class Message(BaseModel):
    username: str
    content: str

class Server(BaseModel):
    content: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(executor())
    yield
    task.cancel()


app = FastAPI(lifespan=lifespan)


@app.post("/message")
def receive_player_message(message: Message):
    perm_router(message)
    return {"status": "ok"}


@app.post("/server")
def receive_server_message(server: Server):
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=config.port)

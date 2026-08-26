from typing import Literal

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from config import config
from graph import executor, perm_router # run executor in main at start


class Message(BaseModel):
    username: str
    message: str


def create_app() -> FastAPI:
    app = FastAPI(title="Noesis")

    @app.post("/message")
    def receive_message(message: Message):
        perm_router(message)
        return "OK"

    return app


app = create_app()


def main() -> None:
    uvicorn.run(app, host="127.0.0.1", port=config.port)


if __name__ == "__main__":
    main()

import argparse
from dataclasses import dataclass


@dataclass
class Config:
    port: int
    env_url: str
    model: str
    name: str


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--env-url", type=str, default="C:/noesis")
    parser.add_argument("--model", type=str, default="openrouter:anthropic/claude-sonnet-4-6")
    parser.add_argument("--name", type=str, default="Noesis")
    args = parser.parse_args()
    return Config(
        port=args.port,
        env_url=args.env_url,
        model=args.model,
        name=args.name,
    )


config = parse_args()

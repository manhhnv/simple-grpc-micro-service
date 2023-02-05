import os
from dotenv import load_dotenv


class Config:
    PORT: int = 0
    GPT_KEY: str = ""

    def __init__(self, vars) -> None:
        if "MODE" in vars and vars["MODE"] == "development":
            self.DEBUG = True
        self.GPT_KEY = vars.get("GPT_KEY", "")
        self.PORT = vars.get("PORT", "50051")


def load() -> Config:
    # load env variables from .env file
    load_dotenv()

    vars = {
        "PORT": int(os.getenv("PORT")),
        "GPT_KEY": os.getenv("GPT_KEY"),
    }
    return Config(vars)

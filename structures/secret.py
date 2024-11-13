from pydantic import BaseModel


class Secret(BaseModel):
    name: str
    path: str

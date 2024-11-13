from pydantic import BaseModel


class Route(BaseModel):
    enabled: bool
    host: str
    path: str = "/"




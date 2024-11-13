from typing import Optional
from pydantic import BaseModel


class Route(BaseModel):
    enabled: bool
    host: Optional[str]
    path: Optional[str] = "/"




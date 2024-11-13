from typing import Optional
from pydantic import BaseModel


class Route(BaseModel):
    enabled: bool
    host: Optional[str] = None
    path: Optional[str] = None




from pydantic import BaseModel
from typing import List, Literal

from structures.env_variables import EnvVariables
from structures.route import Route
from structures.secret import Secret


class Application(BaseModel):
    name: str
    appType: Literal['client' , 'server']
    replicas: int
    containerPort: int
    imageName: str
    imageTag: str
    serviceType: str 
    secrets: List[Secret] = []
    config: EnvVariables 
    disableProbes: bool = False
    route: Route

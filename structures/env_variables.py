from pydantic import BaseModel
from typing import Dict, List



class EnvVariables(BaseModel):
    config: List[Dict[str,str]] = []


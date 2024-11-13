from pydantic import BaseModel, ConfigDict
from typing import List

from consts import DEFAULT_AWS_REGION, DEFAULT_ENV
from structures.application import Application


class Config(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    awsRegion: str = DEFAULT_AWS_REGION
    environment: str = DEFAULT_ENV
    projectName: str

    applications : List[Application]


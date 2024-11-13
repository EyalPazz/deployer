from typing import Any, get_origin, get_args
from pydantic import BaseModel


def is_pydantic_model(annotation: Any) -> bool:
    return isinstance(annotation, type) and issubclass(annotation, BaseModel)


def is_nested_list_of_pydantic_models(annotation) -> bool:
    return get_origin(annotation) is list and is_pydantic_model(get_args(annotation)[0])


def is_list_of_dicts(annotation) -> bool:
    return get_origin(annotation) is list and get_origin(get_args(annotation)[0]) is dict

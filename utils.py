from typer import prompt, confirm

from pydantic_core import PydanticUndefined
from pydantic import BaseModel

from typing import Any, Type, get_args

from consts import LINE_DECORATOR, ADD_NEW_KV, ADD_NEW_OF_FIELD, ENTER_KEY, ENTER_VALUE, ADD_ANOTHER_KV, ENABLED, FALSE

from structures.utils import is_list_of_dicts, is_nested_list_of_pydantic_models, is_pydantic_model


def prompt_fields(model: Type[Any]) -> BaseModel:
    data = {}
    
    for field_name, field in model.model_fields.items():
        field_type = field.annotation
        
        if is_pydantic_model(field_type):
            print(f"{LINE_DECORATOR} {field_type.__name__} {LINE_DECORATOR}")
            data[field_name] = prompt_fields(field_type)
        
        elif is_nested_list_of_pydantic_models(field_type):
            nested_model_type = get_args(field_type)[0]
            data[field_name] = []
            while True:
                add_item = confirm(f"{ADD_NEW_OF_FIELD} {field_name[:-1]}", default=False)
                if not add_item:
                    break
                data[field_name].append(prompt_fields(nested_model_type))

        elif is_list_of_dicts(field_type):
            dict_list = []
            add = confirm(ADD_NEW_KV, default=False)
            while add:
                key = prompt(f"{ENTER_KEY} {field_name}")
                value = prompt(f"{ENTER_VALUE} '{key}'")
                dict_list.append({key: value})
                add = confirm(ADD_ANOTHER_KV, default=False)
            data[field_name] = dict_list

        elif field.default is not PydanticUndefined:
            data[field_name] = prompt(field_name, default=field.default)
        
        else:
            data[field_name] = prompt(field_name)
            if field_name == ENABLED and data[field_name] == FALSE:
                break
    
    return model(**data)

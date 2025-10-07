from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from src.enums.container_actions import ContainerAction

class ContainerRequest(BaseModel):
    container_id: str
    model_config = ConfigDict(alias_generator=to_camel)

class ContainerActionRequest(BaseModel):
    action: ContainerAction
    model_config = ConfigDict(alias_generator=to_camel)
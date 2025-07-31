from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ContainerRequest(BaseModel):
    container_id: str
    model_config = ConfigDict(alias_generator=to_camel)